import cv2 as cv
import mediapipe as mp
import pyautogui
cam = cv.VideoCapture(0)
hand_detect = mp.solutions.hands.Hands()
draw_hand = mp.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()
index_y =0
while True:
    _,frame = cam.read()
    frame = cv.flip(frame,1)
    frame_h,frame_w,_ = frame.shape
    rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output = hand_detect.process((rgb))
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw_hand.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                if id==8:
                    cv.circle(img= frame,center=(x,y),radius=20,color=(0,255,255),thickness=5)
                    index_x = screen_width/frame_w*x
                    index_y = screen_height/ frame_h * x
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv.circle(img= frame,center=(x,y),radius=20,color=(0,255,255),thickness=5)
                    thumb_x = screen_width/frame_w*x
                    thumb_y = screen_height/ frame_h * x
                    if abs(index_y-thumb_y)<20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv.imshow("Mouse",frame)
    cv.waitKey(1)
