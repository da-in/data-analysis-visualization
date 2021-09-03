import csv
import requests
import json

search_query = input('검색어를 입력하세요 : \n')

headers = {
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20200806.01.01'
}

video_headers = {
    'authority': 'www.youtube.com',
    'x-youtube-sts': '18484',
    'x-youtube-device': 'cbr=Chrome&cbrver=84.0.4147.105&ceng=WebKit&cengver=537.36&cos=Macintosh&cosver=10_15_5',
    'x-youtube-page-label': 'youtube.ytfe.desktop_20200805_1_RC1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'x-youtube-variants-checksum': 'a85f7843f63a8b7d2f0e800feae56a8e',
    'x-youtube-page-cl': '325146078',
    'x-spf-referer': 'https://www.youtube.com/results?search_query=%EA%B0%A4%EB%9F%AD%EC%8B%9C+%EB%85%B8%ED%8A%B8+20',
    'x-youtube-utc-offset': '540',
    'x-youtube-client-name': '1',
    'x-spf-previous': 'https://www.youtube.com/results?search_query=%EA%B0%A4%EB%9F%AD%EC%8B%9C+%EB%85%B8%ED%8A%B8+20',
    'x-youtube-client-version': '2.20200806.01.01',
    'dpr': '2',
    'x-youtube-time-zone': 'Asia/Seoul',
    'x-youtube-ad-signals': 'dt=1597134462858&flash=0&frm&u_tz=540&u_his=7&u_java&u_h=1050&u_w=1680&u_ah=1027&u_aw=1680&u_cd=30&u_nplug=3&u_nmime=4&bc=31&bih=948&biw=629&brdim=0%2C23%2C0%2C23%2C1680%2C23%2C1680%2C1027%2C644%2C948&vis=1&wgl=true&ca_type=image',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.youtube.com/results?search_query=%EA%B0%A4%EB%9F%AD%EC%8B%9C+%EB%85%B8%ED%8A%B8+20',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'VISITOR_INFO1_LIVE=JBcPohHFkb8; GPS=1; YSC=uVMfLNJ5nV8; PREF=f4=4000000; ST-1gdf4lt=csn=e1cyX_POJZWU4wKH5ZKYAQ&itct=CIsBENwwGAEiEwil0Ym73pLrAhXTEVgKHcD9DGQyBnNlYXJjaFIT6rCk65-t7IucIOuFuO2KuCAyMJoBAxD0JA%3D%3D',
}

params = (
    ('search_query', search_query),
    ('pbj', '1'),
)

response = requests.get('https://www.youtube.com/results',
                        headers=headers, params=params)


result = json.loads(response.text)

contents = result[1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
    'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

videoId = []

for content in contents:
    keys = list(content.keys())

    if 'videoRenderer' in keys:
        videoId.append(content['videoRenderer']['videoId'])

for vid in videoId:
    params = (
        ('v', vid),
        ('pbj', '1'),
    )

    response = requests.get('https://www.youtube.com/watch',
                            headers=video_headers, params=params)

    result = json.loads(response.text)

    streaming_data = result[2]['playerResponse']['streamingData']['formats'][0]

    if 'url' in streaming_data:
        print(streaming_data['url'])
        with open('./mytube.csv', 'a', encoding='utf-8') as csvfile:
            # 딕셔너리 입력으 위해서 DictWriter 사용
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([streaming_data['url']])
