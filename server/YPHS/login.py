# -*- coding: utf-8 -*-
import requests
import bs4
import json
import hashlib
from YPHS.error import *
import os
import socket
import time

origin_socket=socket.socket


# 密碼的sha256 hash code，如果不知如何取得，請洽開發者
pw_hash = "1dc8229ac5c18df4b736c356d454165a01a80d27e5695390c5419fadb2dc2221"
account = os.environ.get('account',None)
# 資訊股長帳號
pw = os.environ.get('password',None)  # 資訊股長密碼
cls_name = os.environ.get('class',None)  # 導班代號
url = "https://lds.yphs.tp.edu.tw/tea/tua-1.aspx"  # 延平後台網址
with open("./server/YPHS/request.json") as ObjJson:  # 儲存header資訊
    headers_data = json.load(ObjJson)
web = None  # 後台網頁
session = None


def hash(text):
    s = hashlib.sha256()
    s.update(text.encode())
    return s.hexdigest()


def getCookies(cookie_jar):
    '''
    從cookie-jar轉成header傳輸時的字串格式
    '''
    cookie_dict = cookie_jar.get_dict(domain="lds.yphs.tp.edu.tw")
    found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
    return ';'.join(found)


def log_in(password):
    '''
    登入延平後台網站
    '''
    global pw_hash, account, pw, cls_name, headers_data, web, session, url
    if hash(password) != pw_hash:  # 驗證密碼
        raise PasswordError("You're password is wrong.")
    #socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
    socket.socket = socks.socksocket
    url_login = "https://lds.yphs.tp.edu.tw/tea/tua.aspx"
    headers = headers_data["header"]["loadpage"]
    headers1 = headers_data["header"]["login"]
    headers2 = headers_data["header"]["loadagain"]
    variable = {"tbox_acc": account, "tbox_pwd": pw, "tbox_cls": cls_name}
    session = requests.session()
    web_temp = session.get(url_login, headers=headers)
    soup = bs4.BeautifulSoup(web_temp.text, "html.parser")
    for item in headers_data["data"]["login"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    headers1["Cookie"] = getCookies(session.cookies)
    web_temp = session.post(url_login, headers=headers1, data=variable)
    headers2["Cookie"] = getCookies(session.cookies)
    web = session.get(url, headers=headers2)
    if web.url != url:
        raise LogInError("Oops,now you're in " + web.url)


def new_HW(password, title, content, link=""):
    '''
    登錄新的聯絡簿
    '''
    global pw_hash, account, pw, cls_name, headers_data, web, session, url
    if hash(password) != pw_hash:
        raise PasswordError("You're password is wrong.")
    headers = headers_data["header"]["new"]
    headers1 = headers_data["header"]["save"]
    soup = bs4.BeautifulSoup(web.text, "html.parser")
    headers["Cookie"] = getCookies(session.cookies)
    variable = {}
    for item in headers_data["data"]["new"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    web_temp = session.post(url, headers=headers, data=variable)
    headers1["Cookie"] = getCookies(session.cookies)
    soup = bs4.BeautifulSoup(web_temp.text, "html.parser")
    variable = {"tbox_purport": title,
                "tbox_content": content, "tbox_link": link}
    if title == "today":
        variable["tbox_purport"] = soup.find(id="tbox_purport").get("value")
    for item in headers_data["data"]["save"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    web = session.post(url, headers=headers1, data=variable)


def remove_HW(password, target):
    '''
    刪除聯絡簿
    '''
    global pw_hash, account, pw, cls_name, headers_data, web, session, url
    if hash(password) != pw_hash:
        raise PasswordError("The password is wrong.")
    headers = headers_data["header"]["delete"]
    headers["Cookie"] = getCookies(session.cookies)
    soup = bs4.BeautifulSoup(web.text, "html.parser")
    variable = {}
    variable[soup.find_all(value="刪除")[target].get("name")] = "刪除"
    for item in headers_data["data"]["delete"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    web = session.post(url, headers=headers, data=variable)


def change_HW(password, target, title, content, link=""):
    '''
    修改聯絡簿內容
    '''
    global pw_hash, account, pw, cls_name, headers_data, web, session, url
    if hash(password) != pw_hash:
        raise PasswordError("You're password is wrong.")
    headers = headers_data["header"]["change"]
    headers["Cookie"] = getCookies(session.cookies)
    soup = bs4.BeautifulSoup(web.text, "html.parser")
    variable = {}
    variable[soup.find_all(value="修改")[target].get("name")] = "修改"
    for item in headers_data["data"]["change"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    web_temp = session.post(url, headers=headers, data=variable)
    headers1 = headers_data["header"]["save"]
    headers1["Cookie"] = getCookies(session.cookies)
    soup = bs4.BeautifulSoup(web_temp.text, "html.parser")
    variable = {"tbox_purport": title,
                "tbox_content": content, "tbox_link": link}
    for item in headers_data["data"]["save"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    web = session.post(url, headers=headers1, data=variable)


def log_out(password):
    '''
    登出帳號
    '''
    global pw_hash, account, pw, cls_name, headers_data, web, session, url, origin_socket
    if hash(password) != pw_hash:
        raise PasswordError("You're password is wrong.")
    headers = headers_data["header"]["logout"]
    headers["Cookie"] = getCookies(session.cookies)
    soup = bs4.BeautifulSoup(web.text, "html.parser")
    variable = {}
    for item in headers_data["data"]["logout"]:
        if item not in variable:
            variable[item] = soup.find(id=item).get("value")
    web = session.post(url, headers=headers, data=variable)
    web = None
    socket.socket = origin_socket
    time.sleep(5)
