from bs4 import BeautifulSoup
import requests

# AlWAYS CHANGE ONLY THIS PLACE

# MAIN URL
year = 2018
month = 1

MAIN_URL = "https://cbu.uz"
BASE_URL = f"https://cbu.uz/ru/statistics/intlreserves/?arFilter_DATE_ACTIVE_FROM_1=&arFilter_DATE_ACTIVE_FROM_2=&arFilter_ff%5BSECTION_ID%5D=3493&year={year}&month={month}&set_filter=&set_filter=Y"


# AlWAYS CHANGE ONLY THIS PLACE


# statistics: category links for every months

page = requests.get(BASE_URL)
soup = BeautifulSoup(page.text, 'lxml')

parts_links = soup.find_all("div", class_="col-md-6 col-xl-4 mb_30")

# def get_inner_link


# part_links = []
# def get_part_links(url, start_year, end_year, month):
#     for part_link in parts_links:
#         part_links.append(part_link)


lists = []


for part_link in parts_links:
    if part_link:
        part_link = part_link.find("a").get("href")
        lists.append(part_link)
    # else:
    #     month += 1
    #     continue
    # if month <= 13:
    #     year += 1
    #     continue




# def find_download_link(url):
#     links = soup.find(class_="detail-text").find_all("a")

#     # open_link = soup.find("a", text="XLSX")
#     for link in links:
#         link_href_attr =link.get("href")
#         print(link_href_attr)
#     # excel_link = url.find_all("div", class_="col-sm-12 col-12 > a")




for link in lists:
    # print(link)
    detail_url = MAIN_URL + link
    print(MAIN_URL + link)
    download_url = requests.get(detail_url)
    
    print(download_url)



# print(lists)
# get_part_links(BASE_URL, year, 2022, 1)
# print(count)
# print(part_links)
# print(page.status_code)
# print(soup)
