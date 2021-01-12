# 台版最後的克勞迪亞刷首抽腳本,設定為刷到"海盜船+飛艇+沙蟲"停止

詳細的 log 會記錄在同一資料夾的 log.txt 內

---

## 說明

為後台腳本,開啟後使用者可以把模擬器最小化後,腳本依然會進行。

雖然感覺很扯不會有人這樣做,不過還是說一下,請勿把它拿來作為 **商業用途**

---

## 測試環境

#### bluestacks 4.220.0.8005(android 5)

#### 建議為 540x960 解析度,理論上來說支援所有 9x16 解析度

#### 但是解析度過高會導致執行效率過慢&其他問題

只要"模擬器"設定為 540x960 即可,模擬器的大小可以隨意縮放無所謂
android5 版本的 bs 需要下載最新版的 BS 後,使用多開管理器新建多開引擎->全新多開引擎->Lollipop 32-bit

#### python 3.7.9

---

## 使用方法

1.先去下載壓縮檔後解壓縮

|--------重要部分--------|

### 2.然後到"再抽一次"的畫面

![again_screen](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/example.jpg)

是以"![again_btn](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/again.jpg)"為判斷基準

|-----------------------------|

### 3.開啟 Cloudia.exe,如果發現閃退屬於正常現象,因為 adb 還沒有完全啟動,如果閃退的話等個 1~3 秒在重新開啟一次

### 通常要開啟 3 次左右才會成功

PS:如果還是不行,打開 CMD,切換到該資料夾,然後輸入 Cloudia.exe,查看 traceback 後截圖並發出來

---

## 實際執行圖

![example2](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/example2.png)
