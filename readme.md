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

# 0.5 版本

1.先去下載壓縮檔後解壓縮

|--------重要部分--------|

### 2.然後到"再抽一次"的畫面

![](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/example.jpg)

是以"![](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/again.jpg)"為判斷基準

補充:用夜神模擬器的使用者,你們好像要找到夜神專用的 nox_adb.exe,找到後複製一份出來重新命名成 adb.exe,然後覆蓋程式目錄下的 adb 資料夾中的 adb.exe

|-----------------------------|

3.點開"Cloudia.exe",即可開始腳本

---

# 0.6 版本

1.下載源碼後解壓縮

|--------重要部分--------|

### 2.然後到"再抽一次"的畫面

![](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/example.jpg)

是以"![](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/again.jpg)"為判斷基準

|-----------------------------|

3.點擊 start.bat,確認目標設備是否有在選單,沒有的話可以自行添加(可以填入設備名稱,或是全數字的 port 號)

- BS 多開的 port 號,可以去設定->偏好設定->往下拉到 ADB 勾選的那欄->下面黃字有寫說你可以在 127.0.0.1:多少連接,新增 port 號只需輸入":"後面的數字即可

4.如果需要多開則可以再點擊一次 start.bat 並新增腳本工作

- 示範影片:https://youtu.be/o6FgN0pgPgQ

---

## 實際執行圖

![](https://github.com/Zhen-Bo/Cloudia/blob/master/example_image/example2.png)
