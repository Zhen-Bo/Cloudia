import sys
import traceback
import os
__author__ = "Paver(Zhen_Bo)"

# ============================================================================
# 原始解析度 1920x1080
# ============================================================================

print(
    "\033[31mScrpit made by\033[0m \033[41;37mPaver\033[0m,github:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
print(
    "\033[31m此腳本作者為\033[0m \033[41;37mPaver\033[0m,github頁面:\033[37;34mhttps://github.com/Zhen-Bo\033[0m")
print(
    "請問是否為NOX模擬器\n是的話請輸入\033[1;36m\"1\"\033[0m\n不是的話請按\033[1;31mEnter\033[0m")
NOX = input("模式:")
if NOX == "1":
    NOX = True
else:
    NOX = False

try:
    from core.auto import auto
    from core import client
    path = os.path.dirname(os.path.abspath(__file__))
    device = client.get_devices(path, NOX)
    bot = auto(device, NOX)
    bot.bot_start()
except Exception as e:
    error_class = e.__class__.__name__
    detail = e.args[0]
    cl, exe, tb = sys.exc_info()
    lastCallStack = traceback.extract_tb(tb)[-1]
    fileName = lastCallStack[0]
    lineNum = lastCallStack[1]
    funcName = lastCallStack[2]
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(
        fileName, lineNum, funcName, error_class, detail)
    print(errMsg)
    input("按下Enter結束執行")
