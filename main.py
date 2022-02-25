

import time
from selenium import webdriver
import encodings
import requests
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.by import By
import lxml


# file = open('for_save.txt', 'w', encoding='utf-8')
# file.write()
# file_for_save = open('for_save.txt', 'a', encoding='utf-8')

# driver = webdriver.Chrome()
# driver.get("https://www.postavshhiki.ru/")
# time.sleep(2)
# main_page = driver.page_source
# print(type(main_page))
# print(main_page)
# file = open('index.html', 'w', encoding = 'utf-8')
# file.write(main_page)

file = open('index.txt', 'r', encoding='utf-8')
src = file.read()
soup = BeautifulSoup(src,'lxml')
all_div = soup.find('div', class_='otherCatsContainer frontBlockPadding').findAll("a")
all_href_list = []
all_href_dict = {}
all_href_name_list = []

for i in all_div:
    text = f'{i.text} - "https://www.postavshhiki.ru"{i.get("href")}'
    href = f'https://www.postavshhiki.ru{i.get("href")}'
    # file_for_save.write(text)
    all_href_list.append(href)
    all_href_dict[i.text.strip()] = {}
    all_href_dict[i.text.strip()]["link"] = href
    all_href_name_list.append(i.text.strip())


# count = 0
# for href_elem in all_href_list:
#     count += 1
#     driver = webdriver.Chrome()
#     driver.get(href_elem)
#     page = driver.page_source
#     file = open(f'Page\page_{count}.html', 'w', encoding = 'utf-8')
#     file.write(page)

all_link_list = []
for page_elem in range(1,26):
    link_list = []
    page_now = f'Page\page_{page_elem}.html'
    page_now_for_save = f'Page\page_for_save_{page_elem}.txt'
    file_now = open(page_now, 'r', encoding='utf-8')
    # file_now_for_save = open(page_now_for_save, 'w', encoding='utf-8')
    src = file_now.read()
    soup = BeautifulSoup(src, 'lxml')
    all_link = soup.findAll('div', class_ = 'compInfoBlock')
    for div_elem in all_link:
        div_elem_href = div_elem.findAll('a')
        for div_elem_href_elem in div_elem_href:
            link = 'https://www.postavshhiki.ru'+ div_elem_href_elem.get("href")
            text_for_save = f'{div_elem_href_elem.text} - {link} \n'
            # file_now_for_save.write(text_for_save)
            link_list.append(link)
            all_href_dict[all_href_name_list[page_elem-1]][div_elem_href_elem.text] = {}
            all_href_dict[all_href_name_list[page_elem - 1]][div_elem_href_elem.text]["link"] = link
    all_link_list.append(link_list)

# file_json = open('dict_json.json', 'w', encoding='utf-8')
# file_json.write(json.dumps(all_href_dict, indent=4, ensure_ascii=False, sort_keys=True))
# print(json.dumps(all_href_dict, indent=4, ensure_ascii=False, sort_keys=True))

for list_elem in all_link_list:
    for elem in list_elem:
        driver = webdriver.Chrome()
        driver.get(elem)
        page = driver.page_source




