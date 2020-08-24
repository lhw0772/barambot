import cv2

import telegram
from telegram.ext import Updater, CommandHandler
import baram
import threading
import pyautogui
import numpy as np
from config import *

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = ID
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def sendImage(self, img):
        self.core.send_photo(chat_id = self.id,photo = img)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class BotBaram(TelegramBot):
    def __init__(self):
        self.token = TOKEN
        TelegramBot.__init__(self, '바람', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('바람 봇이 잠에서 깨어납니다.')
        self.updater.start_polling()
        self.updater.idle()

import sys
import time

def get_screencapture():
    pic = pyautogui.screenshot(region=(0, 0, 1280, 720))
    img_frame = np.array(pic)
    img_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2RGB)
    output_name = 'screen.png'
    cv2.imwrite(output_name, img_frame)
    return  output_name



def monitoring():
    baraminfo = baram.BaramInfo()

    sleepTime = 1

    while (1):
        is_abnormal = False

        time.sleep(sleepTime)

        result = baraminfo.get_data('die')

        if (result == True):
            botbaram.sendMessage('케릭터가 사망하였습니다.')
            output_name = get_screencapture()
            botbaram.sendImage(open(output_name, 'rb'))

        if result :
            is_abnormal = True

        result = baraminfo.get_data('repair')

        if (result == True):
            botbaram.sendMessage('내구도가 바닥났습니다.')
            output_name = get_screencapture()
            botbaram.sendImage(open(output_name, 'rb'))

        if result :
            is_abnormal = True

        if is_abnormal:
            sleepTime = 60 * 10
        else:
            sleepTime = 1


def proc_monitor(bot,update):
    botbaram.sendMessage('케릭터 사망/내구도 모니터링 시작합니다.')
    t1 = threading.Thread(target=monitoring)
    t1.start()

def proc_img(bot, update):
    baraminfo = baram.BaramInfo()
    dat= baraminfo.get_data('exp')
    output_name = 'output.png'
    cv2.imwrite(output_name,dat)
    botbaram.sendImage(open(output_name,'rb'))

def proc_stop(bot, update):
    botbaram.sendMessage('바람 봇이 잠듭니다.')
    botbaram.stop()

def proc_screenshot(bot, update):
    botbaram.sendMessage('현재 화면입니다.')
    output_name = get_screencapture()
    botbaram.sendImage(open(output_name, 'rb'))



botbaram = BotBaram()
botbaram.add_handler('exp', proc_img)
botbaram.add_handler('stop', proc_stop)
botbaram.add_handler('monitor', proc_monitor)
botbaram.add_handler('screen',proc_screenshot)
botbaram.start()