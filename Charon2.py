from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (1200,1100))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)

    print(value)

    drone.takeoff()
    drone.land()