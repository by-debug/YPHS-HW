from apscheduler.schedulers.asyncio import AsyncIOScheduler
from time import timezone
from datetime import datetime
import os
import asyncio
import websockets

scheduler = AsyncIOScheduler(timezone="Asia/Taipei")

url = f"wss://{os.environ.get('name',None)}.herokuapp.com/0.0.0.0"

async def ping():
    async with websockets.connect(url) as websocket:
         await websocket.send("ping")
         rec = await websocket.recv()
    print(rec)


async def main():
    global scheduler
    scheduler.add_job(ping, "cron", hour="8-22", day_of_week='mon-fri')
    scheduler.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()


