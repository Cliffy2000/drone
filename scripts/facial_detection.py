import cv2
import time
import asyncio
from djitellopy import Tello
from threading import Thread


drone = Tello()
drone.connect()
airborne = False

battery = drone.get_battery()
print(f'Drone battery at {battery}%.')
if battery <= 15:
    print("Battery too low.")
    quit()
else:
    drone.streamon()
    stream = True


async def camera_feed():
    # This function needs to run at all times to provide
    # constant video stream
    await asyncio.sleep(0)
    while True:
        # Upon activating, the cv2 library would report error messages
        # due to image feed not yet received
        frame = drone.get_frame_read().frame
        img = cv2.resize(frame, (300, 200))
        cv2.imshow("result", img)

        global stream
        if not stream:
            return


async def drone_control():
    i = 0
    while True:
        print(i)
        i += 1


drone.streamon()
def i():
    while True:
        frame = drone.get_frame_read()
        f = frame.frame
        img = cv2.resize(f, (300, 200))
        cv2.imshow("result", img)


r = Thread(target=i)
r.start()


drone.end()
