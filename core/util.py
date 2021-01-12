from cv2 import cv2
from core import adb

adbkit = adb.adbKit()


def compare(img_path, target_img):
    gatcha = []
    # 海
    ship = cv2.imread("{0}/ship.jpg".format(img_path))
    result = cv2.matchTemplate(target_img, ship, cv2.TM_CCOEFF_NORMED)
    reslist = cv2.minMaxLoc(result)
    if reslist[1] > 0.9:
        gatcha.append("海盜船雷古尼斯號")
    # 飛
    space = cv2.imread("{0}/space.jpg".format(img_path))
    result = cv2.matchTemplate(target_img, space, cv2.TM_CCOEFF_NORMED)
    reslist = cv2.minMaxLoc(result)
    if reslist[1] > 0.9:
        gatcha.append("飛艇隆瓦裡歐號")
    # 沙
    sand = cv2.imread("{0}/sand.jpg".format(img_path))
    result = cv2.matchTemplate(target_img, sand, cv2.TM_CCOEFF_NORMED)
    reslist = cv2.minMaxLoc(result)
    if reslist[1] > 0.9:
        gatcha.append("超砂獸的靈帝牙")
    return gatcha


def get_width_muti():
    sample = adbkit.screenshots(raw=True)
    adbkit.capmuti = sample.shape[0] / 1920


def standby(template, img_path, acc=0.85):
    target_img = adbkit.screenshots()
    find_img = cv2.imread(str(template))
    # 模板匹配
    result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
    reslist = cv2.minMaxLoc(result)
    if reslist[1] > acc:
        pos = [reslist[3][0], reslist[3][1]]
        pos = [x*adbkit.capmuti for x in pos]
        return pos, compare(img_path, target_img)
    else:
        return False


def tap(pos, raw=False):
    if raw:
        adbkit.click(pos[0], pos[1], raw=True)
    else:
        adbkit.click(pos[0], pos[1])
