import cv2  # image
import time  # delay
import imutils  # resize
from datetime import datetime  # for timestamp
from playsound import playsound
import threading

cam = cv2.VideoCapture(0)  # cam id
time.sleep(1)

firstFrame = None
area = 500
alarm_playing = False
alarm_thread = None

def play_alarm():
    global alarm_playing
    while alarm_playing:
        playsound("alarm.wav")

while True:
    _, img = cam.read()  # read frame from camera
    text = "Normal"
    img = imutils.resize(img, width=500)  # resize

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # color to Gray scale image

    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # smoothened

    if firstFrame is None:
        firstFrame = gaussianImg  # capturing 1st frame on 1st iteration
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # absolute diff b/w 1st and current frame

    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]  # binary

    threshImg = cv2.dilate(threshImg, None, iterations=2)

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"
        
        # Start playing alarm if not already playing
        if not alarm_playing:
            alarm_playing = True
            alarm_thread = threading.Thread(target=play_alarm)
            alarm_thread.start()

    print(text)
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("o"):  # if 'O' key is pressed
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"captured_image_{timestamp}.png"
        cv2.imwrite(filename, img)  # save the image with a unique filename
        print(f"Image captured and saved as '{filename}'")
    
    if key == ord("s"):  # if 'S' key is pressed
        alarm_playing = False
        if alarm_thread is not None:
            alarm_thread.join()  # wait for the alarm thread to finish
        print("Alarm stopped")

    if key == ord("q"):  # if 'Q' key is pressed
        break

cam.release()
cv2.destroyAllWindows()
