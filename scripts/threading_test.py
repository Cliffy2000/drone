import threading
from djitellopy import Tello
import cv2
import time


# drone = Tello()
# drone.connect()
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# drone.streamon()


def camera():
    while True:
        frame = drone.get_frame_read()
        f = frame.frame

        gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(f, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("img", f)

        if cv2.waitKey(1) & 0xFF == 27:
            break


def control():
    time.sleep(5)
    #drone.takeoff()
    while True:
        key = cv2.waitKey(1) & 0xff
        if key == 27:  # ESC
            break
        elif key == ord('w'):
            print('w')
    #drone.land()


if __name__ == "__main__":
    thread1 = threading.Thread(target=camera)
    thread2 = threading.Thread(target=control)
    #thread1.start()
    thread2.start()
