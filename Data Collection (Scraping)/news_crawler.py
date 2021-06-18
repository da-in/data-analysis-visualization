import csv
import requests
from bs4 import BeautifulSoup

result = []

with open('./news_result.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['news_title', 'news_link'])

for start_num in range(1, 102, 10):
    search = '펜트하우스'
    URL = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=65&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={start_num}'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_list = soup.select(
        '#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

    for news in news_list:
        # print(f"news : {news} \n\n\n")

        # 링크 가져오기
        news_data = news.select_one('div > div > a.news_tit')
        news_link = news_data['href']
        news_title = news_data['title']
        # result.append([news_title, news_link])
        # print(f"{news_title} , {news_link} \n")

        with open('./news_result.csv', 'a', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([news_title, news_link])
