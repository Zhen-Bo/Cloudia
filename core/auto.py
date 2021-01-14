import os
import time
from core import util


class auto():
    def __init__(self):
        self.log = open('log.txt', 'a')
        self.line = "//================================================\n"
        self.ship_flag = False
        self.space_flag = False
        self.sand_flag = False
        self.times = 0
        self.path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))) + "/images"

    def log_info(self, str):
        self.log.write(str)
        print(str, end='')

    def bot_start(self):
        # os.system('cls')
        try:
            util.adbkit.get_width_muti()
        except:
            raise Exception("請確認模擬器是否為android5版本")
        self.log_info(self.line)
        self.log_info("開始運行\n")
        self.log_info(self.line)
        POG = []
        again = False
        again = util.standby("{0}/again.jpg".format(self.path), self.path)
        try:
            util.tap(again[0], raw=True)
        except:
            raise Exception("沒有偵測到\"再抽一次\",或是解析度不是9x16的解析度\n退出程式")
        time.sleep(0.5)
        while len(POG) != 3:
            t_start = time.time()
            POG = []
            again = False
            while not again:
                again = util.standby(
                    "{0}/again.jpg".format(self.path), self.path)
                if not again:
                    util.tap((960, 70))
            POG = again[1]
            if self.times == 0:
                self.times += 1
            elif self.times != 0:
                self.log_info("第{0}次結果:\n".format(self.times))
                if len(POG) > 0:
                    self.log_info('命中數量: {0}\n'.format(len(POG)))
                    for i in range(len(POG)):
                        self.log_info("{0}.{1}\t".format(i+1, POG[i]))
                    self.log_info('\n')
                else:
                    self.log_info('命中數量: 0\n')
                t_end = time.time()
                cost_time = round(t_end-t_start, 2)
                if cost_time > 3:
                    self.log_info("耗時 {0} 秒\n".format(cost_time))
                    self.log_info(self.line)
                else:
                    continue
                if len(POG) != 3:
                    util.tap(again[0], raw=True)
                    time.sleep(1)
                    self.times += 1
                elif len(POG) == 3:
                    print("執行結束,總共執行 {0} 次".format(self.times))
                    enter = input("請輸入enter繼續")
                    break
