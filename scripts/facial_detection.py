import cv2
import time
import asyncio
from djitellopy import Tello


marker = 0


async def camera_feed():
    while True:
        print(f'------')
        if marker == 1:
            return
        await asyncio.sleep(0)


async def drone_control():
    for i in range(10000):
        print(f'   {i}   ')
        if i > 6000:
            global marker
            marker = 1
            return
        await asyncio.sleep(0)


async def main():
    task_camera = asyncio.create_task(camera_feed())
    task_drone = asyncio.create_task(drone_control())

    await task_camera
    await task_drone


if __name__ == "__main__":
    drone = Tello()
    drone.connect()

    battery = drone.get_battery()
    print(f'Drone battery at {battery}%.')
    if battery <= 15:
        print("Battery too low.")
        quit()

    try:
        asyncio.run(main())
    finally:
        drone.emergency()
        print("Drone motors off.")

    drone.end()
