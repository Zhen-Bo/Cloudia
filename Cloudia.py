import sys
import traceback
import os
__author__ = "Paver(Zhen_Bo)"

# ============================================================================
# 原始解析度 1920x1080
# ============================================================================

try:
    from core.auto import auto
    from core import client
    path = os.path.dirname(os.path.abspath(__file__))
    device = client.get_devices(path)
    bot = auto(device, debug=True)
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
