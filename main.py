"""
Project : AI Virtual Mouse
Developer : Chanchal Roy
Date : 27th Oct 2022
GitHub : https://github.com/codewithcc/AI-Virtual-Mouse
"""
import HandDec
import cv2
import pyautogui
import numpy
# import time

frameR = 30
plocX, plocY = 0, 0
clocX, clocY = 0, 0
smoothening = 2
pyautogui.FAILSAFE = False
wScr, hScr = pyautogui.size()

if __name__ == '__main__':
    # timeS = time.time()
    mp = HandDec.HandDetector(max_hands=1)
    cam = mp.init_cam()

    while cam.isOpened():
        success, frame = cam.read()
        if not success: continue
    ##############################################
        mp.findHand(frame, draw_detect=False)
        myHands, bBox = mp.findLocations(frame, draw_id=8, draw_detect=False)
        if myHands:
            fingerState = mp.fingerUp()
            # print(fingerState)
            if fingerState[1] == 1 and fingerState[2] == 0:
                # print('Finger is Up!')
                # print(myHands)
                hCam, wCam, _ = frame.shape
                x1, y1 = myHands[8][1], myHands[8][2]
                x3 = numpy.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y3 = numpy.interp(y1, (frameR, hCam - frameR), (0, hScr))
                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening
                pyautogui.moveTo(wScr - clocX, clocY)
                plocX, plocY = clocX, clocY

            if fingerState[1] == 1 and fingerState[2] == 1:
                distance = mp.findDistance(frame, 8, 12, draw_detect=False)
                # print(distance)
                if distance < 0.05:
                    pyautogui.click(wScr - clocX, clocY)
    ##############################################
        # timeE = time.time()
        # fps = int(1 / (timeE - timeS))
        # timeS = timeE
        # cv2.putText(frame, str(f'FPS : {fps}'), (20, 40), 0, 1.5, (0, 255, 0), 3)
        cv2.imshow('AI Virtual Mouse', cv2.flip(frame, 1))
        if cv2.waitKey(1) & 0xff == ord('q'): break

    cam.release()
    cv2.destroyAllWindows()
