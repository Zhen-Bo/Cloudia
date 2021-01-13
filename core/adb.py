import os
import subprocess
import numpy as np
import time
from cv2 import cv2


class adbKit(object):
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.system("{0}/adb/adb.exe kill-server".format(self.path))
        os.system("{0}/adb/adb.exe start-server".format(self.path))
        print("等待10秒讓ADB載入模擬器")
        for i in range(11):
            print(10-i, " ", end='\r')
            time.sleep(1)
        print("    ")
        os.system("{0}/adb/adb.exe devices".format(self.path))
        self.capmuti = float(1)

    def debug_get_write(self):
        pipe = subprocess.Popen("{0}/adb/adb.exe shell screencap -p".format(self.path),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        image_bytes = pipe.stdout.read()
        print(image_bytes[0:10])
        image_bytes = image_bytes.replace(b'\r\r\n', b'\n')
        print(image_bytes[0:10])
        image = cv2.imdecode(np.frombuffer(
            image_bytes, dtype='uint8'), cv2.IMREAD_COLOR)
        image = cv2.imwrite("screencap.png", image)
        raw = input("按Enter鍵繼續debug")

    def debug_read(self):
        image = cv2.imread("screencap.png")
        print(image.shape)
        raw = input("按Enter鍵關閉視窗")

    def get_width_muti(self):
        sample = self.screenshots(raw=True)
        try:
            self.capmuti = sample.shape[0] / 1920
        except:
            print("無法取得解析度")

    def screenshots(self, raw=False):
        pipe = subprocess.Popen("{0}/adb/adb.exe shell screencap -p".format(self.path),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        image_bytes = pipe.stdout.read()
        image_bytes = image_bytes.replace(b'\r\r\n', b'\n')
        time.sleep(0.5)
        image = cv2.imdecode(np.frombuffer(
            image_bytes, dtype='uint8'), cv2.IMREAD_COLOR)
        if image.shape[0] != 1920 and image.shape[1] != 1080 and not raw:
            image = self.reimage(image)
        return image

    # DONE 多解析度支援

    def reimage(self, images):
        images = cv2.resize(images, (1080, 1920))
        return images

    def click(self, pointx, pointy, raw=False):
        if raw:
            Px = str(pointx)
            Py = str(pointy)
        else:
            Px = str(int(pointx)*self.capmuti)
            Py = str(int(pointy)*self.capmuti)
        os.system(
            "{0}/adb/adb.exe shell input tap ".format(self.path) + ' ' + Px + ' ' + Py)
