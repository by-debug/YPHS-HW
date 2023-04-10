# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def word_of_today():
    header = {"Upgrade-Insecure-Requests": "1",
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
              "AppleWebKit/537.36 (KHTML, like Gecko)"
              " Chrome/92.0.4515.131 Safari/537.36",
              }
    web = requests.get(
        "https://www.merriam-webster.com/word-of-the-day", headers=header)
    soup = BeautifulSoup(web.text, "html.parser")
    return (soup.find("div", class_="word-header").find("h2").text,
            soup.find("div", class_="wod-definition-container").find("p").text)


if __name__ == "__main__":
    a = word_of_today()
    print(a)
