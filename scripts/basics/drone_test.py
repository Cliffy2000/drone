from djitellopy import Tello


def main_test():
    drone.takeoff()
    drone.land()


if __name__ == "__main__":
    drone = Tello()
    drone.connect()

    main_test()

    drone.emergency()
    drone.end()
