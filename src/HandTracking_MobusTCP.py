import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
 
class handTracking():
    def __init__(self,index = 0):
        self.cap = cv2.VideoCapture(index)
        self.pTime = 0
        self.detector = htm.handDetector(detectionCon=0.7)
    def videoCapture(self):
        ret, img = self.cap.read()
        if ret:
            img = self.detector.findHands(img)
            lmList = self.detector.findPosition(img, draw=False)
            if len(lmList) != 0:
                # print(lmList[4], lmList[8])
        
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        
                self.length = math.hypot(x2 - x1, y2 - y1)
                
                if self.length < 50:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 0), 3)
            cv2.imshow("Img", img)
            cv2.waitKey(1)
        else:
            return -1

    def outputData(self):
        return int(self.length)