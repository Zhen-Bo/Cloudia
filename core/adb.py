import os
import subprocess
import numpy as np
from cv2 import cv2


class adbKit(object):
    def __init__(self) -> None:
        self.capmuti = float(1)
        os.system("/adb/adb.exe start-server")

    def screenshots(self, raw=False):
        pipe = subprocess.Popen("/adb/adb.exe shell screencap -p",
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        image_bytes = pipe.stdout.read().replace(b'\r\r\n', b'\n')
        image = cv2.imdecode(np.frombuffer(
            image_bytes, dtype='uint8'), cv2.IMREAD_COLOR)
        if image.shape[0] != 1920 and image.shape[1] != 1080 and not raw:
            image = self.reimage(image)
        return image

    # TODO 多解析度支援
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
        os.system('/adb/adb.exe shell input tap ' + Px + ' ' + Py)
