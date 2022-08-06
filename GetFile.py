# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:24:59 2021

@author: chrai
"""
import requests
from bs4 import BeautifulSoup as bs

qu ='GLYCERIN'
qq='Sodium Acrylates Crosspolymer-2'
def incide2(ingre_name):
    what_it_does = []
    alias = []
    irritancy, comedogenicity, rank = '', '', ''
    n_i=do_alpha(ingre_name)
    r = requests.get('https://incidecoder.com/ingredients/'+n_i)
    soup=bs(r.text,"html.parser")
    aloha = soup.find("h1")
    if (aloha.text == "Sorry, this page does not seem to exist"):
        return n_i, what_it_does, irritancy, comedogenicity, 'nothing', alias
    try:
        rank = soup.find("div", class_="ourtake grey1").text.strip()
    except:
        rank=''
    try:
        soup_list=soup.find_all("div",class_="itemprop")
    except:
        return n_i, what_it_does,irritancy,comedogenicity, rank ,alias
    try:
        for i in range(len(soup_list)):
            try:
                what_it_do=soup_list[i].select("a")
                for j in range(len(what_it_do)):
                    what_it_does.append(what_it_do[j].getText().replace('\u200b', "").strip())
            except:
                print(Exception.__name__)
            try:
                if(soup_list[i].select_one("span.label.klavikab.grey1").text == 'Also-called-like-this:'):
                    str= soup_list[i].select_one("span.value").text.strip()
                    alias = str.split(", ")
                    for a in alias:
                        a = a.replace('\u200b', "")
                        a = a.strip()
                if (soup_list[i].select_one("span.label.klavikab.grey1").text == 'Irritancy: '):
                    irritancy = soup_list[i].select_one("span.value").text.strip()
                if (soup_list[i].select_one("span.label.klavikab.grey1").text == 'Comedogenicity: '):
                    comedogenicity = soup_list[i].select_one("span.value").text.strip()
            except:
                print(Exception.__name__)
        return n_i, what_it_does,irritancy,comedogenicity, rank , alias
    except:
        print(Exception.__name__)

def do_alpha(ing):
    search = ''
    ing = ing.replace('\u200b', "")
    for a in ing:
        if (a.isalnum()):
            search += a.lower()
        elif (a == "/" or a == "-" or a == "," or a == " " or a == "[" or a == "]"):
            search += "-"
    return search
"""
在抓的到excel資料後，可將其設為變數，
再用用for迴圈，一直跑incide跟climbincide去爬資料，將查到的資料放進資料表，
但是要設if-else去過濾找不到的要存進資料庫的值為何。
"""
print(incide2(qu))