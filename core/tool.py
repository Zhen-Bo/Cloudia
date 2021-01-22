import os
import subprocess
import numpy as np
from cv2 import cv2
import time


class adbKit():
    def __init__(self, device, NOX=False, debug=False) -> None:
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.debug = debug
        self.capmuti = 1
        self.device = device
        if NOX:
            self.adb_path = "{}/adb/nox/nox_adb.exe".format(self.path)
        else:
            self.adb_path = "{}/adb/adb.exe".format(self.path)
        self.breakline = self.get_SDK().encode('utf-8')

    def debug_get_write(self):
        t1 = time.time()
        pipe = subprocess.Popen("{0} -s {1} shell screencap -p".format(self.adb_path, self.device),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        image_bytes = pipe.stdout.read()
        print(image_bytes[0:10])
        image_bytes = image_bytes.replace(self.breakline, b'\n')
        print(image_bytes[0:10])
        t2 = time.time()
        image = cv2.imdecode(np.frombuffer(
            image_bytes, dtype='uint8'), cv2.IMREAD_COLOR)
        print("耗時 {0} 秒".format(round(t2-t1, 2)))
        cv2.imwrite("screenshot.png", image)
        input("按Enter鍵關閉視窗")

    def get_SDK(self):
        SDK_version = subprocess.Popen("{0} -s {1} shell getprop ro.build.version.release".format(
            self.adb_path, self.device), stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        SDK_version = SDK_version.stdout.read().decode("utf-8")
        if int(SDK_version[0]) >= 7:
            return '\r\n'
        elif int(SDK_version[0]) <= 5:
            return '\r\r\n'
        else:
            print("不是android5或android7")

    def screenshots(self, raw=False):
        pipe = subprocess.Popen("{0} -s {1} shell screencap -p".format(self.adb_path, self.device),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        image_bytes = pipe.stdout.read()
        image_bytes = image_bytes.replace(self.breakline, b'\n')
        image = cv2.imdecode(np.frombuffer(
            image_bytes, dtype='uint8'), cv2.IMREAD_COLOR)
        if image.shape[0] != 1920 and image.shape[1] != 1080 and not raw:
            image = self.reimage(image)
        return image

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
        if self.debug:
            print('[ADB]adb shell input tap ' + Px + ' ' + Py)
        os.system(
            '{0} -s {1} shell input tap {2} {3}'.format(self.adb_path, self.device, Px, Py))

    def swipe(self, x1, y1, x2, y2, delay):
        cmdSwipe = '{0} -s {1} shell input swipe {2} {3} {4} {5} {6}'.format(
            self.adb_path, self.device, int(x1), int(y1), int(x2), int(y2), int(delay*1000))
        if self.debug:
            print('[ADB]adb shell swipe from X:{0} Y:{1} to X:{2} Y:{3} Delay:{4}'.format(
                int(x1), int(y1), int(x2), int(y2), int(delay*1000)))
        os.system(cmdSwipe)


class tool():
    def __init__(self, device, NOX, img_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images"), debug=False) -> None:
        self.debug = debug
        self.adbkit = adbKit(device, NOX)
        self.adbkit.capmuti = self.get_width_muti()
        self.screenshot = None
        self.ark = self.get_ark(img_path)
        self.template = self.load_template(img_path, self.ark)

    def get_width_muti(self):
        sample = self.adbkit.screenshots(raw=True)
        return sample.shape[0] / 1920

    def get_ark(self, path):
        arks = []
        for img in os.listdir(path):
            arks.append(img)
        arks.remove("again.jpg")
        choose = []
        while True:
            os.system('cls')
            print(
                "\033[31mScrpit made by\033[0m \033[41;37mPaver\033[0m,github:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
            print(
                "\033[31m此腳本作者為\033[0m \033[41;37mPaver\033[0m,github頁面:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
            i = 1
            print("目前候選名單: ", end='')
            for ark in arks:
                print("{0}.{1}    ".format(i, ark.split('.')[0]), end='')
                i += 1
            print("\n目前已選名單: ", end='')
            j = 1
            for ark in choose:
                print("{0}.{1}    ".format(j, ark.split('.')[0]), end='')
                j += 1
            print("\n輸入a為全部添加,輸入e離開")
            index = input("請輸入要鎖定的聖物編號: ")
            try:
                index = int(index)
                if index > len(arks):
                    print("超出最大編號")
                    input("請按enter繼續選擇")
                    continue
                choose.append(arks[index-1])
                arks.remove(arks[index-1])
            except:
                if index.lower() == 'a':
                    for ark in arks:
                        choose.append(ark)
                    arks = []
                elif index.lower() == 'e':
                    os.system('cls')
                    print(
                        "\033[31mScrpit made by\033[0m \033[41;37mPaver\033[0m,github:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
                    print(
                        "\033[31m此腳本作者為\033[0m \033[41;37mPaver\033[0m,github頁面:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
                    print("\n目前已選名單: ", end='')
                    j = 1
                    for ark in choose:
                        print("{0}.{1}    ".format(
                            j, ark.split('.')[0]), end='')
                        j += 1
                    ctr = input("\n確定選擇請按enter,重新選擇請輸入'n': ")
                    if str(ctr).lower() == 'n':
                        return self.get_ark(path)
                    else:
                        return choose
                else:
                    continue
            finally:
                if len(arks) == 0:
                    os.system('cls')
                    print(
                        "\033[31mScrpit made by\033[0m \033[41;37mPaver\033[0m,github:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
                    print(
                        "\033[31m此腳本作者為\033[0m \033[41;37mPaver\033[0m,github頁面:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
                    print("\n目前已選名單: ", end='')
                    j = 1
                    for ark in choose:
                        print("{0}.{1}    ".format(
                            j, ark.split('.')[0]), end='')
                        j += 1
                    ctr = input("\n確定選擇請按enter,重新選擇請輸入'n': ")
                    if str(ctr).lower() == 'n':
                        return self.get_ark(path)
                    else:
                        return choose

    def load_template(self, img_path, template_list):
        imgs = []
        for template in template_list:
            img = os.path.join(img_path, template)
            imgs.append(self.cv_read(img))
        return imgs

    def compare(self, img_list, gach=False, acc=0.85):
        imgs = []
        self.screenshot = self.adbkit.screenshots()
        for item in img_list:
            imgs.append(cv2.imread(item))
        for img in imgs:
            find_height, find_width = img.shape[:2:]
            result = cv2.matchTemplate(
                self.screenshot, img, cv2.TM_CCOEFF_NORMED)
            reslist = cv2.minMaxLoc(result)
            if self.debug:
                cv2.rectangle(self.screenshot, reslist[3], (
                    reslist[3][0]+find_width, reslist[3][1]+find_height), color=(0, 250, 0), thickness=2)
            if reslist[1] > acc:
                if self.debug:
                    print("[Detect]acc rate:", round(reslist[1], 2))
                pos = [reslist[3][0], reslist[3][1]]
                pos = [x*self.adbkit.capmuti for x in pos]
                if gach == True:
                    return pos, self.gatcha()
                else:
                    return pos
        return False

    def cv_read(self, file_path):
        img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        return img

    def gatcha(self):
        gatcha = []
        for index in range(len(self.template)):
            result = cv2.matchTemplate(
                self.screenshot, self.template[index], cv2.TM_CCOEFF_NORMED)
            result = cv2.minMaxLoc(result)
            if result[1] > 0.9:
                gatcha.append(self.ark[index])
        return gatcha

    def tap(self, pos, raw=False):
        if raw:
            self.adbkit.click(pos[0], pos[1], raw=True)
        else:
            self.adbkit.click(pos[0], pos[1])

    def swipe(self, x1, y1, x2, y2, delay):
        self.adbkit.swipe(x1, y1, x2, y2, delay)
