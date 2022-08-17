# YPHS-HW

##### 延平中學聯落簿登錄系統

此軟體可將當日聯絡簿的內容排版後登錄至延平中學的網路聯絡簿，並在聯絡簿後方加上每日一詞。（來源：[Merriam-Webster Dictionary](https://www.merriam-webster.com/)）可配延平的電子班牌或電腦教室的電腦使用（使用前請告知並徵求導師同意）

#### 特色

1. 自動排版
2. 自動爬取每日一詞，放置在聯絡簿後方
3. 可從資料庫抓取歷史作業
4. 自動排版
5. 不易因連線時間長而導致登出。就算登出後也會保留之前登錄的作業。
6. 可使用自己的密碼，不必記憶學校配發的密碼（更改方式：將server/YPHS/login.py第15行之pw_hash

#### 開始使用(Server端)（使用heroku示範）

1. 將此專案fork至您自己的github帳號
2. 在[heroku](https://dashboard.heroku.com/)建立帳號，並建立一個新的dyno
![](https://i.imgur.com/LPHFY4W.png)

3. 點進設定(settings)，到Config Vars選項，點選Reveal Config Vars![](https://i.imgur.com/t3ERW3I.png)點開之後，新增四個變數：account、password、class和name，分別填入學校資訊股長登入的帳號、密碼、班級代碼和APP名稱。（就是你剛剛建立dyno的時候用的名稱）![](https://i.imgur.com/q9xtX1c.png)

4. 點選Config Vars下方的Buildpacks選項，點選Add Buildpacks之後![](https://i.imgur.com/hkFV75F.png)，點選python。![](https://i.imgur.com/fyA3LXA.png)

5. 進入Resources，在Add-ons的搜尋框中搜尋postgres，點選Heroku Postgres，![](https://i.imgur.com/an36nwW.png)選擇方案（預設為免費方案）後直接確認。![](https://i.imgur.com/FouTTYK.png)

6. 點選deploy，在deployment method選擇github。![](https://i.imgur.com/maFD0SC.png)接著你應該會需要登入github帳戶。登入完成後，選擇fork來的專案，就可以將其部署上heroku了。




#### 開始使用（client端）

##### 下載可執行檔（Windows）

1. 從github中的release選擇一個最新版（:warning: 2.0.0版之前的版本已經棄用）
![](https://i.imgur.com/5Q3gBID.png)
2. 下載並解壓縮zip檔
3. 將其中的url一檔案以文字編輯器打開後，將url改成你的dyno的網址（應可在執行畫面找到）![](https://i.imgur.com/uME19Gs.png)。以此處為例，你需要將url內的網址改成 yphs-hw-test.herokuapp.com (:warning:不要加https://)
4. 照著應用程式裡的說明開始使用

##### 下載原始檔

1. 確定你的電腦中安裝python，並安裝了websockets套件
2. 在Github Repository中點選Code按鈕，使用git下載或者直接下載zip檔並解壓縮![](https://i.imgur.com/xSE1xBE.png)
3.  在終端機中開啟client資料夾
4. 依據你的作業系統，執行以下命令：

Windows:
```bash=
python client.py
```

MacOs or Linux:
```bash=
python3 client.py
```


關於以上說明，如果有任何問題，或者你發現有任何bug，請在Issue中提出，或者直接email到by20051002@gmail.com。
