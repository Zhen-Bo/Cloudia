import os
import time
from datetime import datetime
from core.tool import tool


class auto():
    def __init__(self, device):
        try:
            port = device.split(":")[1]
        except:
            port = device
        self.log = open('log-{0}.txt'.format(port), 'a')
        self.line = "//================================================\n"
        self.ship_flag = False
        self.space_flag = False
        self.sand_flag = False
        self.times = 0
        self.path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))) + "/images"
        self.adbtool = tool(device)
        self.start = None
        self.end = None

    def log_info(self, str):
        self.log.write(str)
        print(str, end='')

    def bot_start(self):
        self.log_info(self.line)
        self.start = datetime.now()
        self.log_info("開始運行,開始時間: {}\n".format(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.log_info(self.line)
        POG = []
        again = False
        again = self.adbtool.compare(
            ["{0}/again.jpg".format(self.path)], self.path)
        try:
            self.adbtool.tap(again, raw=True)
        except:
            raise Exception("沒有偵測到\"再抽一次\",或是解析度不是9x16的解析度\n退出程式")
        time.sleep(0.5)
        while len(POG) != len(self.adbtool.ark):
            t_start = time.time()
            POG = []
            again = False
            while not again:
                again = self.adbtool.compare(
                    ["{0}/again.jpg".format(self.path)], gach=True)
                if not again:
                    self.adbtool.tap((960, 70))
            POG = again[1]
            t_end = time.time()
            cost_time = round(t_end-t_start, 2)
            if self.times == 0:
                self.times += 1
            elif self.times != 0 and cost_time > 5:
                self.log_info("第{0}次結果:\n".format(self.times))
                if len(POG) > 0:
                    self.log_info('命中數量: {0}\n'.format(len(POG)))
                    for i in range(len(POG)):
                        self.log_info("{0}.{1}\t".format(i+1, POG[i]))
                    self.log_info('\n')
                else:
                    self.log_info('命中數量: 0\n')
                self.log_info("耗時 {0} 秒\n".format(cost_time))
                self.log_info(self.line)
                if len(POG) != len(self.adbtool.ark):
                    self.adbtool.tap(again[0], raw=True)
                    time.sleep(1)
                    self.times += 1
                elif len(POG) == len(self.adbtool.ark):
                    self.end = datetime.now()
                    print(
                        "執行結束,總共執行 {0} 次, 結束時間 {1} ,共花費 {2} ".format(self.times, self.end, str(self.end-self.start)))
                    input("請輸入enter繼續")
                    break
