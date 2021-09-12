# -*- coding: utf-8 -*-
import websockets
import asyncio
from YPHS.webster import word_of_today
from YPHS.error import *
from YPHS.mydatabase import database
from YPHS.login import log_in, new_HW
import getpass
import datetime

table_name = "HW107"

line = "----------------------------------------------------------------------------------------\n"
tab = "     "


def get_content(db, date=datetime.datetime.now().strftime(
        '%Y/%m/%d')):
    global table_name, line, tab
    HW = db.select(table_name, date)  # (id,type,day,subject,content)"
    subjects = {"ch": "國文", "en": "英文", "ma": "數學", "ph": "物理", "che": "化學", "bi": "生物", "es": "地科",
                "hi": "歷史", "ge": "地理", "ci": "公民", "co": "電腦", "cr": "生科", "mu": "音樂", "ar": "美術", "ht": "導師", "coa": "輔導"}
    HWs = {}
    tests = {}
    exams = {}
    notes = {}
    link = ""
    for i in HW:
        if i[1] == "0":
            if i[3] not in HWs:
                HWs[i[3]] = [i[4]]
            else:
                HWs[i[3]].append(i[4])
        elif i[1] == "1":
            if i[3] not in tests:
                tests[i[3]] = [i[4]]
            else:
                tests[i[3]].append(i[4])
        elif i[1] == "2":
            if i[3] not in exams:
                exams[i[3]] = [i[4]]
            else:
                exams[i[3]].append(i[4])
        elif i[1] == "3":
            if i[3] not in notes:
                notes[i[3]] = [i[4]]
            else:
                notes[i[3]].append(i[4])
        else:
            link = i[4]
    content = ""
    content += line
    content += "作業：\n"
    i = 1
    for subject, HW in HWs.items():
        content += str(i) + ". "
        content += "（" + subjects[subject] + "）"
        if len(HW) == 1:
            content += HW[0] + '\n'
        else:
            j = 1
            content += '\n'
            for item in HW:
                content += tab + "（" + str(j) + "）" + item + '\n'
                j += 1
        i += 1
    i = 1
    content += line
    content += "小考：\n"
    for subject, test in tests.items():
        content += str(i) + ". "
        content += "（" + subjects[subject] + "）"
        if len(test) == 1:
            content += test[0] + '\n'
        else:
            j = 1
            content += '\n'
            for item in test:
                content += tab + "（" + str(j) + "）" + item + '\n'
                j += 1
        i += 1
    i = 1
    content += line
    content += "週考或段考：\n"
    for subject, exam in exams.items():
        content += str(i) + ". "
        content += "（" + subjects[subject] + "）"
        if len(exam) == 1:
            content += exam[0] + '\n'
        else:
            j = 1
            content += '\n'
            for item in exam:
                content += tab + "（" + str(j) + "）" + item + '\n'
                j += 1
        i += 1
    i = 1
    content += line
    content += "提醒事項：\n"
    for subject, note in notes.items():
        content += str(i) + ". "
        content += "（" + subjects[subject] + "）"
        if len(note) == 1:
            content += note[0] + '\n'
        else:
            j = 1
            content += '\n'
            for item in note:
                content += tab + "（" + str(j) + "）" + item + '\n'
                j += 1
        i += 1
    return content,link


def run(table_name, query):
    db = database("Homework.db")
    if type(query) != list:
        raise YPHSError
    if query[0] == "add":
        db.insert(table_name, query[2], query[1], query[3])
    elif query[0] == "add_old":
        result = db.select_by_id(table_name, query[1])
        db.insert(table_name, result[3], result[1], result[4])
    elif query[0] == "change":
        db.update(table_name, query[1], query[2])
    elif query[0] == "show":
        if query[1] == "today":
            content,link = get_content(db)
        else:
            content,link = get_content(db, query[1])
            return content + '\n' + line + "連結：\n" + link
    elif query[0] == "show_id":
        if query[1]!="today":
            return db.select(table_name,query[1])
        else:
            return db.select(table_name,datetime.datetime.now().strftime(
        '%Y/%m/%d'))
    elif query[0] == "remove":
        db.delete(table_name, query[1])
    elif query[0] == "submit":
        log_in(query[2])
        content,link = get_content(db)
        content += line
        content += "每日一詞：\n"
        word = word_of_today()
        content += word[0] + '\n'
        content += "-> " + word[1] + '\n'
        content += "(from Webster's Dictionary)\n"
        new_HW(query[2], query[1], content, link)
        del db
    else:
        del db
        raise InputSyntaxError("Please check that you use the right syntax.")


async def reply(websocket, path):
    message = await websocket.recv()
    print(f"< {message}")
    try:
        ret = run(table_name, message.split())
    except YPHSError as e:
        ret = e
    if ret == None:
        ret = "finished!"
    await websocket.send(str(ret))
    print(f"> {ret}")

if __name__ == "__main__":
    start_server = websockets.serve(reply, "0.0.0.0", 443)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
