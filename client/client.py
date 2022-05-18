# -*- coding: utf-8 -*-
import ssl
import getpass
from pprint import pprint
from ast import literal_eval
from sys import exit
import warnings
import socketio
warnings.filterwarnings("ignore")

greet = """
您好。歡迎使用此聯絡簿登錄系統。
在使用此軟體前，請先詳閱說明並遵守以下語法規範：
（不須輸入引號）

add \"類型\" \"科目\" \"內容\"
add_old \"id_1\" \"id_2\" （新增區間：[id_1,id_2]）
show \"日期\"(如果想看今天的聯絡簿，可輸入today)
show_id \"日期\"(如果想看今天的聯絡簿，可輸入today)
change \"id\" \"text\"
remove \"id_1\" \"id_2\" （刪除區間：[id_1,id_2]）
submit \"title\"(如果直接使用延平預設標題，則輸入today)
quit

記得，輸入日期的格式為：yyyy/mm/dd（如果只有個位數要補零）（ex. 2022/02/03、1905/01/20......）

P.S.
類型:
0. 功課
1. 小考
2. 週考或段考
3. 提醒事項
4. 附件連結

科目：
chi: 國文
eng: 英文
mat: 數學
phy: 物理
che: 化學
bio: 生物
geos: 地科
his: 歷史
geo: 地理
cit: 公民
com: 電腦
lif: 生科
mus: 音樂
art: 美術
hrt: 導師
coa: 輔導
me: 資訊股長提醒
exp: 探究實作
pe: 體育
"""

ssl_context = ssl.SSLContext()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

socio = socketio.Client()

@socio.on("to client")
def recv(data):
    if data["data"][0] == '[' and data["data"][-1] == ']':
        pprint(literal_eval(data["data"]))
    else:
        print(data["data"])


if __name__ == "__main__":
    print(greet)
    with open("url","r") as file:
        url = "https://"+file.read()
    socio.connect(url)
    while True:
        msg = input("請輸入指令：")
        if msg[0:4] == "quit":
            socio.disconnect()
            exit(0)
        if msg[0:6] == "submit":
            pw = getpass.getpass("請輸入密碼：")
            socio.emit("recv",msg+" "+pw)
        else:
            socio.emit("recv",msg)
