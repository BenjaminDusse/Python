import requests

from time import sleep
from bs4 import BeautifulSoup

years = [2018, 2019, 2020, 2021, 2022]
month = 1

MAIN_URL = "https://cbu.uz"
BASE_URL = "https://cbu.uz/ru/statistics/intlreserves/?arFilter_DATE_ACTIVE_FROM_1=&arFilter_DATE_ACTIVE_FROM_2=&arFilter_ff%5BSECTION_ID%5D=3493&year={}&month={}&set_filter=&set_filter=Y"


links = []
count = 0

def get_links(years):
    """ This function gets all links from detail pages """
    for y in years:
        for i in range(12):
            url = BASE_URL.format(y, i+1)
            # print(url)
            req = requests.get(url)
            sleep(0.5)
            # print(req.text)
            soup = BeautifulSoup(req.text, 'lxml')
            # parts_links = soup.find_all("div", class_="col-md-6 col-xl-4 mb_30")
            # print(len(parts_links))
            # qwe = soup.find_all("div", class_="col-md-6 col-xl-4 mb_30")
            links_layout = soup.find_all('a', class_='link_box')
            print(f"{len(links_layout)} data pages found")
            for ll in links_layout:
                links.append(ll.get("href"))
            global count
            count += 1
            if count <=50:
                break
            # break
        # break



get_links(years)
print(f"User can send only {count} requests into platform")

def download_excel_files():
    """ This function downloads all excel files """
    count = 1
    for link in links:
        url = MAIN_URL + link
        # print(url)
        # break
        req = requests.get(url)
        sleep(0.5)
        soup = BeautifulSoup(req.text, 'lxml')
        file_links = soup.find('div', class_='news-detail').find_all('a')
        # print(len(file_links))
        custom_list = [fl.get("href") for fl in file_links]
        # print(custom_list)
        # for get excel file link
        get_excel_link = list(filter(lambda l: l.endswith(".xlsx"), custom_list))
        if get_excel_link:
            req = requests.get(MAIN_URL + get_excel_link[0])
            # print(req)
            with open(f"{count}.xlsx", "wb") as file:
                file.write(req.content)
            count += 1

for i in range(50):
    download_excel_files()

# optimallashtirish
# try except
# adminkani excelga import export qilish using export library

# pip install django jazzmin for beautifull admin
