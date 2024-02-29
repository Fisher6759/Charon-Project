from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
drone.takeoff()
drone.streamon()
print(drone.get_battery())


#Looks like the while loop that is the main problem.

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (1060,1040))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)

    print(value)

    if value == "A":
        drone.rotate_clockwise(90)
        drone.move_forward(20)
        drone.land()
    #elif value == "B":
       # drone.rotate_clockwise(-90)
        #drone.move_backward(20)
        #drone.land()
    #elif value == "C":
        #drone.rotate_clockwise(180)
        #drone.move_forward(30)
        #drone.land()
   # elif value == "D":
     #   drone.rotate_clockwise(-180)
      #  drone.move_backward(30)
       # drone.land()
    else:
        drone.land()