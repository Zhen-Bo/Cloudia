import subprocess
import os


def read_devices(path):
    devices = subprocess.Popen("{0}/adb/adb.exe devices".format(path),
                               shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
    lists = devices.split("\n")
    devicesNames = []
    for item in lists:
        if(item.strip() == ""):
            continue
        elif (item.startswith("List of")):
            continue
        else:
            devicesNames.append(item.split("\t")[0])
    return devicesNames


def select_devices(path, devicesIds):
    os.system('cls')
    print("請選擇你要控制的設備:")
    i = 1
    for deviceId in devicesIds:
        print("\033[1;34m {0}:{1}\033[0m".format(i, deviceId))
        i += 1
    print("\033[1;36m a: 新增\033[0m")
    print("\033[1;31m e: 離開\033[0m")
    try:
        inputIndex = input(
            "請輸入編號 [1 ~ {0}]:".format(i-1))
        value = int(inputIndex)
        if value < 1 or value >= i:
            raise Exception("編號過大")
        return devicesIds[value - 1]
    except (KeyboardInterrupt, SystemExit):
        raise Exception("KeyboardInterrupt")
    except Exception as e:
        if "e" == inputIndex.lower():
            return -1
        elif "a" == inputIndex.lower():
            port = input("請輸入設備名稱或連接在127.0.0.1的port: ")
            if port.isdigit():
                os.system(
                    "{0}/adb/adb.exe connect 127.0.0.1:{1}".format(path, port))
            else:
                os.system("{0}/adb/adb.exe connect {1}".format(path, port))
            input("輸入enter繼續")
            return select_devices(path, read_devices(path))
        else:
            print(
                "\033[1;31m編號輸入錯誤,請在試一次\033[0m")
            input("請輸入enter繼續")
            return select_devices(path, devicesIds)


def get_devices(path):
    devices = read_devices(path)
    client = select_devices(path, devices)
    if client == -1:
        raise Exception("使用者終止")
    return client
