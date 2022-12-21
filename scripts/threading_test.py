import threading
from djitellopy import Tello
import cv2
import time


drone = Tello()
drone.connect()

drone.streamon()


def camera():
    while True:
        frame = drone.get_frame_read()
        f = frame.frame
        cv2.imshow("img", f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            drone.land()
            print(f'battery: {drone.get_battery()}')
            break


def control():
    time.sleep(5)
    drone.takeoff()
    time.sleep(1)
    drone.land()


if __name__ == "__main__":
    try:
        thread1 = threading.Thread(target=camera)
        thread2 = threading.Thread(target=control)
        thread1.start()
        thread2.start()
    finally:
        drone.land()