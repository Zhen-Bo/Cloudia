import os
from core import util
import time


class auto():
    def __init__(self):
        self.log = open('log.txt', 'a')
        self.line = "//================================================\n"
        util.get_width_muti()
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
        self.log_info(self.line)
        self.log_info("開始運行\n")
        self.log_info(self.line)
        POG = []
        again = False
        again = util.standby("{0}/again.jpg".format(self.path), self.path)
        util.tap(again[0], raw=True)
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
                self.log_info("耗時 {0} 秒\n".format(cost_time))
                self.log_info(self.line)
                self.times += 1
                time.sleep(1)
                util.tap(again[0], raw=True)
        print("執行結束,總共執行 {0} 次".format(self.times))
