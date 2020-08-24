import cv2 as cv
import numpy as np
import pyautogui
from config import *

class BaramInfo:
    def __init__(self):
        self.exp_gt = cv.imread(EXP_GT, cv.IMREAD_COLOR)
        self.exp_h, self.exp_w = self.exp_gt.shape[:2]
        self.die_gt = cv.imread(DIE_GT, cv.IMREAD_COLOR)
        self.die_h, self.die_w = self.die_gt.shape[:2]
        self.repair_gt = cv.imread(REPAIR_GT, cv.IMREAD_COLOR)
        self.repair_h, self.repair_w = self.repair_gt.shape[:2]

    def get_data(self,question):

        if question == 'exp':
            pic = pyautogui.screenshot(region=(0, 0, 430, 720))
        elif question == 'die':
            pic = pyautogui.screenshot(region=(0, 0, 1280, 720))
        elif question == 'repair':
            pic = pyautogui.screenshot(region=(800, 0, 480, 360))
        else:
            pic = pyautogui.screenshot(region=(0, 0, 1280, 720))

        img_frame = np.array(pic)
        img_frame = cv.cvtColor(img_frame, cv.COLOR_BGR2RGB)
        meth = 'cv.TM_CCOEFF'
        method = eval(meth)

        if question == 'exp':
            gt = self.exp_gt
            w =  self.exp_w
            h = self.exp_h

        elif question == 'die':
            gt = self.die_gt
            w =  self.die_w
            h = self.die_h

        elif question == 'repair':
            gt = self.repair_gt
            w =  self.repair_w
            h = self.repair_h

        res = cv.matchTemplate(gt, img_frame, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        x,y= top_left
        cropped_img = img_frame[y: y + h, x: x + w]
        print(question, max_val, top_left)
        img_frame = cv.rectangle(img_frame,top_left,bottom_right,(255,0,0))

        if question == 'exp':
            return cropped_img
        elif question == 'die':
            if(max_val>die_th):
                cv.imwrite('dielog.png',img_frame)
                return True
            else:
                return False
        elif question =='repair':
            if (max_val > repair_th):
                cv.imwrite('repairlog.png', img_frame)
                return True
            else:
                return False


# barambot = BaramInfo()
# cv.imshow('test',barambot.get_data('exp'))
# cv.waitKey(0)
#
# barambot = BaramInfo()
# while(1):
#     print (barambot.get_data('die'))

# barambot = BaramInfo()
# while (1):
#     barambot.get_data('repair')