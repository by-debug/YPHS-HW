from string import Template
from datetime import datetime
import requests
import psycopg2
import os

url = os.environ.get("DATABASE_URL")

def get_current_time():
    site=requests.get("https://worldtimeapi.org/api/timezone/Asia/Taipei")
    data=site.json()
    day=datetime.fromisoformat(data["datetime"])
    return day.strftime('%Y/%m/%d')


class database:
    def __init__(self, name):
        global usr, psw, dt2
        self.name = name
        self.db = psycopg2.connect(url)

    def __del__(self):
        global usr, psw
        self.db.commit()
        self.db.close()

    def create_table(self, table_name):
        cur = self.db.cursor()
        cur.execute(Template("SELECT EXISTS(SELECT * from information_schema.tables WHERE table_name = '$name' )").substitute(name=table_name))
        if not cur.fetchone()[0]:
            cur.execute(Template(
                "CREATE TABLE $name(id SERIAL PRIMARY KEY,type TEXT,day TEXT,subject TEXT,content TEXT)").substitute(name=table_name))
        cur.close()

    def insert(self, table_name, subject, type_, content):
        cur = self.db.cursor()
        cur.execute(Template("INSERT INTO $name(type , day , subject , content ) VALUES('$type' , '$dat' , '$subject' , '$txt' )").substitute(
            name=table_name, dat=get_current_time(), type=type_, subject=subject, txt=content))
        self.db.commit()
        cur.close()

    def select(self, table_name, date):
        cur = self.db.cursor()
        results = cur.execute(Template(
            "SELECT * FROM $name WHERE day='$day'").substitute(name=table_name, day=date))
        cur.close()
        return results.fetchall()

    def select_by_id(self, table_name, id):
        cur = self.db.cursor()
        result = cur.execute(Template(
            "SELECT * FROM $name WHERE id='$no'").substitute(name=table_name, no=id)).fetchone()
        cur.close()
        return result

    def update(self, table_name, id, content):
        cur = self.db.cursor()
        cur.execute(Template("UPDATE $name SET content = '$content' WHERE id = '$id'").substitute(
            name=table_name, id=id, content=content))
        self.db.commit()
        cur.close()

    def delete(self, table_name, id):
        cur = self.db.cursor()
        cur.execute(Template("DELETE FROM $name WHERE id='$id'").substitute(
            name=table_name, id=id))
        self.db.commit()
        cur.close()
