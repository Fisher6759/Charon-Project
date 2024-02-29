from djitellopy import tello
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()
drone.move_forward(450)
drone.land()