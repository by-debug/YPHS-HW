# YPHS-HW

##### 延平中學聯落簿登錄系統

此軟體可將當日聯絡簿的內容排版後登錄至延平中學的網路聯絡簿，並在聯絡簿後方加上每日一詞。（來源：[Merriam-Webster Dictionary](https://www.merriam-webster.com/)）可配延平的電子班牌或電腦教室的電腦使用（使用前請告知並徵求導師同意）

#### 開始使用(Server端)（使用heroku示範）

1. 將此專案fork至您自己的github帳號
2. 在[heroku](https://dashboard.heroku.com/)建立帳號，並建立一個新的dyno
![](https://i.imgur.com/LPHFY4W.png)

3. 點進設定(settings)，到Config Vars選項，點選Reveal Config Vars![](https://i.imgur.com/t3ERW3I.png)點開之後，新增三個變數：account、password和class三個變數，分別填入學校資訊股長登入的帳號、密碼和班級代碼。![](https://i.imgur.com/q9xtX1c.png)

4. 點選Config Vars下方的Buildpacks選項，點選Add Buildpacks之後![](https://i.imgur.com/hkFV75F.png)，點選python。![](https://i.imgur.com/fyA3LXA.png)

5. 點選deploy，在deployment method選擇github。![](https://i.imgur.com/maFD0SC.png)接著你應該會需要登入github帳戶。登入完成後，選擇fork來的專案，就可以將其部署上heroku了。




#### 開始使用（client端）

1. 從github中的release選擇一個你喜歡的版本下載
2. 解壓縮符合你的作業系統的zip
3. 將其中的url一檔案以文字編輯器打開後，將url改成你的dyno的網址（應可在執行畫面找到）![](https://i.imgur.com/uME19Gs.png)+0.0.0.0。以此處為例，你需要將url內的網址改成 yphs-hw-test.herokuapp.com/.0.0.0.0
4. 照著應用程式裡的說明開始使用

關於以上說明，如果有任何問題，或者你發現有任何bug，請在Issue中提出，或者直接email到by20051002@gmail.com。
