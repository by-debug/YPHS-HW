# YPHS-HW

##### 延平中學聯落簿登錄系統

此軟體可將當日聯絡簿的內容排版後登錄至延平中學的網路聯絡簿，並在聯絡簿後方加上每日一詞。（來源：[Merriam-Webster Dictionary](https://www.merriam-webster.com/)）可配延平的電子班牌或電腦教室的電腦使用（使用前請告知並徵求導師同意）

#### 開始使用(Server端)（使用repl.it示範）

1. 將此專案fork至您自己的github帳號
2. 在[replit](https://replit.com/)建立帳號，並建立一個新的repl

![step2](https://i.imgur.com/fVcz8fw.png)

3. 選擇"import from github"，並選擇本專案之fork

![step3](https://i.imgur.com/s0iARUa.png)

4. 按照指示設定語言為python，並將執行路徑設為

```bash=
python ./server/server.py
```

![step4](https://i.imgur.com/XKswekd.png)

5. 按下run，先讓系統設定好python環境，此時應會因為錯誤而停止]
6. 設定環境變數：account（延平中學資訊股長登入帳號）、password（延平中學資訊股長登入密碼）、class（延平中學導班代號）、ftpusr（yphs ftp的帳號）、ftppsw（yphs ftp的密碼）

![step6](https://i.imgur.com/6ztcn8n.png)

7. 在yphs ftp中，新增一個資料夾叫database
8. 按下右手邊shell，輸入以下程式碼

```bash=
cd server/YPHS
python setup.py
```

![step8](https://i.imgur.com/SsuM2AH.png)

9. 將login.py中第10行的pw_hash改成你所想要密碼的sha256
10. 按下run

#### 開始使用（client端）

1. 從github中的release選擇一個你喜歡的版本下載
2. 解壓縮zip
3. 照著應用程式裡的說明開始使用

關於以上說明，如果有任何問題，或者你發現有任何bug，請在Issue中提出，或者直接email到by20051002@gmail.com
