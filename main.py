from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import random
from openpyxl import load_workbook
import requests

def magic(url):

    for i in range(1, 1000):
        skT = skoliko_tel('https://www.inmyroom.ru/profi/page/', i)
        #driver_servise = Service(executable_path='D:\\programming\\Case888\\Python\\Парсинг проекты\\www.inmyroom.ru\\chromedriver.exe')
        driver = webdriver.Chrome(executable_path='D:\\programming\\Case888\\Python\\pars_pro\\www__inmyroom__ru\\chromedriver.exe')
        driver.get(url + f"{i}")
        time.sleep(13)

        print(skT)
        for j in range(skT):
            button = driver.find_element(By.XPATH, '//a[@data-el="UserContacts/show"]')
            button.click()
            time.sleep(random.randint(2, 5))

        time.sleep(10)
        with open("index_selenium10.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        driver.close()
        with open("index_selenium10.html", "r", encoding="utf-8") as file:
            file = file.read()

        soup = BeautifulSoup(file, "lxml")

        listEnd = []
        YES = soup.find_all('div', class_="user-preview user-preview__default")
        for p in YES:
            perexod = []
            name = p.find('a', class_="user-preview_name")
            telefon = p.find('div', class_="user-contacts_phone")
            uRl = p.find('a', class_="user-contacts_site")
            sity = p.find('div', class_="user-preview_city")

            perexod.append(name.text)
            if telefon != None:
                perexod.append(telefon.text)
            else:
                perexod.append('NONE')

            if uRl != None:
                perexod.append(uRl.text)
            else:
                perexod.append('NONE')

            if sity != None:
                perexod.append(sity.text)
            else:
                perexod.append('NONE')

            listEnd.append(perexod)


        fn = 'Microsoft Excel.xlsx'
        wb = load_workbook(fn)
        ws = wb['Аркуш1']
        for l in listEnd:
            ws.append(l)
        wb.save(fn)
        wb.close()

        time.sleep(4)




def skoliko_tel(url, i):

    url1 = url + f"{i}"

    headers = {'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.888 Yowser/2.5 Safari/537.36'
               }
    req = requests.get(url1, headers=headers)

    soupchik = BeautifulSoup(req.text, "lxml")
    g = soupchik.find_all('a', {'data-el':"UserContacts/show"})
    return len(g)











def main():
    magic('https://www.inmyroom.ru/profi/page/')






if __name__ == '__main__':
    main()