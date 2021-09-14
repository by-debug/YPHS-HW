import sqlite3
from string import Template
import datetime


class database:
    def __init__(self, name):
        self.db = sqlite3.connect(name)

    def __del__(self):
        self.db.commit()
        self.db.close()

    def create_table(self, table_name):
        self.db.cursor()
        self.db.execute(Template(
            "CREATE TABLE $name(id INTEGER PRIMARY KEY AUTOINCREMENT,type TEXT,day TEXT,subject TEXT,content TEXT)").substitute(name=table_name))

    def insert(self, table_name, subject, type_, content):
        self.db.execute(Template("INSERT INTO $name(type , day , subject , content ) VALUES(\"$type\" , \"$dat\" , \"$subject\" , \"$txt\" )").substitute(
            name=table_name, dat=datetime.datetime.now().strftime('%Y/%m/%d'), type=type_, subject=subject, txt=content))
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
