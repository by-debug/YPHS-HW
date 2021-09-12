# -*- coding: utf-8 -*-
import asyncio
import websockets
import pathlib
import ssl
import getpass
from pprint import pprint

greet = """
您好。歡迎使用此聯絡簿登錄系統。
在使用此軟體前，請先詳閱說明並遵守以下語法規範：
（不須輸入引號）

add \"類型\" \"科目\" \"內容\"
add_old \"id\"
show \"日期\"
change \"id\" \"text\"
remove \"id\"
submit \"title\"

P.S.
類型:
0. 功課
1. 小考
2. 週考或段考
3. 提醒事項
4. 附件連結

科目：
ch: 國文
en: 英文
ma: 數學
ph: 物理
che: 化學
bi: 生物
es: 地科
hi: 歷史
ge: 地理
ci: 公民
co: 電腦
cr: 生科
mu: 音樂
ar: 美術
ht: 導師
coa: 輔導
"""

ssl_context = ssl.SSLContext()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


async def query():
    uri = "wss://YPHS-HW.bydebug.repl.co"
    command = input("請輸入指令：")
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        if command[0:6] == "submit":
            pw = getpass.getpass("請輸入密碼：")
            await websocket.send(command + ' ' + pw)
        else:
            await websocket.send(command)
        print(f"> {command}")
        rec = await websocket.recv()
        pprint(rec)


if __name__ == "__main__":
    print(greet)
    while True:
        asyncio.get_event_loop().run_until_complete(query())
