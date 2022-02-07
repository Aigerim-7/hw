from django.contrib.sites import requests
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup


HOST = "https://onlinemultfilmy.ru/"
URL = "https://onlinemultfilmy.ru/latest1"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36 Edg/97.0.1072.69'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='t-item')
    cartoon = []


    for item in items:
        cartoon.append(
            {
                'title': item.find('div', class_='t-item').get_text(),
                'image': HOST + item.find('div', class_="t-item-img").find('img').get('src')
            }
        )
    return cartoon


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cartoon = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            cartoon.extend(get_data(html.text))
            return cartoon
    else:
        raise ValueError('Error in parser function')