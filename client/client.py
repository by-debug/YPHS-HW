# -*- coding: utf-8 -*-
import ssl
import getpass
from pprint import pprint
from ast import literal_eval
from sys import exit
import warnings
import websockets
import asyncio
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
art: 美術
hrt: 導師
coa: 輔導
me: 資訊股長提醒
pe: 體育
"""

ssl_context = ssl.SSLContext()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def query():
    with open("url","r") as file:
        url = "wss://"+file.read()
    command = input("請輸入指令：")
    async with websockets.connect(url, ssl=ssl_context) as websocket:
        if command[0:4] == "quit":
            exit(0)
        if command[0:6] == "submit":
            pw = getpass.getpass("請輸入密碼：")
            await websocket.send(command + ' ' + pw)
        else:
            await websocket.send(command)
        print(f"> {command}")
        rec = await websocket.recv()
        print(rec)
        if rec[0] == '[' and rec[-1] == ']':
            pprint(literal_eval(rec))
        else:
            print(rec)


if __name__ == "__main__":
    print(greet)
    while True:
        asyncio.get_event_loop().run_until_complete(query())
