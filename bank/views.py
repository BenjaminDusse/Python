import requests
from django.shortcuts import render
from src.find import get_links, download_excel_files

from time import sleep
from bs4 import BeautifulSoup

years = [2018, 2019, 2020, 2021, 2022]
month = 1

MAIN_URL = "https://cbu.uz"
BASE_URL = "https://cbu.uz/ru/statistics/intlreserves/?arFilter_DATE_ACTIVE_FROM_1=&arFilter_DATE_ACTIVE_FROM_2=&arFilter_ff%5BSECTION_ID%5D=3493&year={}&month={}&set_filter=&set_filter=Y"


def home(request):
    links = []

    count = 0
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
            count += 1
    context = {
        'links': links
    }
    return render(request, 'index.html', context)

