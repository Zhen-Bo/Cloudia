import os
import subprocess
import numpy as np
import time
from cv2 import cv2


class adbKit(object):
    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.system("{0}/adb/adb.exe start-server".format(self.path))
        print("請稍候5秒")
        time.sleep(5)
        os.system("{0}/adb/adb.exe start-server".format(self.path))
        self.capmuti = float(1)

    def get_width_muti(self):
        sample = self.screenshots(raw=True)
        try:
            self.capmuti = sample.shape[0] / 1920
        except:
            print("無法取得解析度")

    def screenshots(self, raw=False):
        # pipe = subprocess.Popen("{0}/adb/adb.exe shell screencap -p".format(self.path),
        #                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        # image_bytes = pipe.stdout.read()
        # image_bytes = image_bytes.replace(b'\r\r\n', b'\n')
        # time.sleep(0.5)
        os.system(
            '{0}/adb/adb.exe shell screencap -p /sdcard/screencap.png'.format(self.path))
        os.system('{0}/adb/adb.exe pull /sdcard/screencap.png'.format(self.path))
        image = cv2.imread(self.path + "/screencap.png")
        try:
            if image.shape[0] != 1920 and image.shape[1] != 1080 and not raw:
                image = self.reimage(image)
            return image
        except:
            time.sleep(1)

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
