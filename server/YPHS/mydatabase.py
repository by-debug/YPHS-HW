import sqlite3
from string import Template
from datetime import datetime
from ftplib import FTP
import requests
import os


usr = os.environ['ftpusr']
psw = os.environ['ftppsw']

def get_current_time():
    site=requests.get("https://worldtimeapi.org/api/timezone/Asia/Taipei")
    data=site.json()
    day=datetime.fromisoformat(data["datetime"])
    return day.strftime('%Y/%m/%d')

def remote_connect(server, file_name, usr, psw):
    server.set_debuglevel(0)
    server.connect("203.72.178.240")
    server.login(usr, psw)
    server.cwd("./database")
    with open(f"./{file_name}", "wb") as w:
        server.retrbinary(f'RETR ./{file_name}', w.write)
    server.quit()


def remote_upload(server, file_name, usr, psw):
    server.set_debuglevel(2)
    server.connect("203.72.178.240")
    server.login(usr, psw)
    server.cwd("./database")
    with open(f"./{file_name}", "rb") as r:
        server.storbinary(f"STOR ./{file_name}", r)
    server.quit()


class database:
    def __init__(self, name):
        global usr, psw, dt2
        self.name = name
        self.server = FTP()
        try:
            remote_connect(self.server, name, usr, psw)
        except:
            pass
        self.db = sqlite3.connect(name)

    def __del__(self):
        global usr, psw
        self.db.commit()
        self.db.close()
        remote_upload(self.server, self.name, usr, psw)

    def create_table(self, table_name):
        self.db.cursor()
        self.db.execute(Template(
            "CREATE TABLE $name(id INTEGER PRIMARY KEY AUTOINCREMENT,type TEXT,day TEXT,subject TEXT,content TEXT)").substitute(name=table_name))

    def insert(self, table_name, subject, type_, content):
        self.db.execute(Template("INSERT INTO $name(type , day , subject , content ) VALUES(\"$type\" , \"$dat\" , \"$subject\" , \"$txt\" )").substitute(
            name=table_name, dat=get_current_time(), type=type_, subject=subject, txt=content))
        self.db.commit()

    def select(self, table_name, date):
        results = self.db.execute(Template(
            "SELECT * FROM $name WHERE day=\"$day\"").substitute(name=table_name, day=date))
        return results.fetchall()

    def select_by_id(self, table_name, id):
        result = self.db.execute(Template(
            "SELECT * FROM $name WHERE id=\"$no\"").substitute(name=table_name, no=id)).fetchone()
        return result

    def update(self, table_name, id, content):
        self.db.execute(Template("UPDATE $name SET content = \"$content\" WHERE id = \"$id\"").substitute(
            name=table_name, id=id, content=content))
        self.db.commit()

    def delete(self, table_name, id):
        self.db.execute(Template("DELETE FROM $name WHERE id=\"$id\"").substitute(
            name=table_name, id=id))
        self.db.commit()
