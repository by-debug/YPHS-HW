import asyncio
import websockets
import ssl

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

P.S. type:
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
ch: 化學
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
"""

async def query():
    uri = "wss://YPHS-HW.bydebug.repl.co"
    ws = websockets.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    async with ws.connect(uri) as websocket:
        command = input("請輸入指令")

        await websocket.send(command)
        print(f"> {command}")

        rec = await websocket.recv()
        print(f"< {rec}")


if __name__ == "__main__":
  print(greet)
  asyncio.get_event_loop().run_until_complete(query())
