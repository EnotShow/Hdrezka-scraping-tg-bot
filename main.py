from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


def get_releases():
    url = 'https://rezka.ag'
    ua = UserAgent
    response = requests.get(
        url=url,
        headers={'user-agent': f'ua.random'}
    )

    response = response.text

    # with open('index.html', 'w', encoding='UTF-8') as file:
    #     file.write(response)

    # with open('index.html', encoding='UTF-8') as file:
    #     scr = file.read()

    message_list = []

    soup = BeautifulSoup(response, 'lxml')

    get_some = soup.find(class_='b-seriesupdate__block').find(class_='b-seriesupdate__block_list')
    get_href = soup.find(class_='b-seriesupdate__block').find(class_='b-seriesupdate__block_list').find_all('a')

    cycle = 0

    for i in get_some:
        if i.text == '':
            cycle += 1
            continue
        message_list.append(i.text + f" https://rezka.ag{get_href[cycle].get('href')}")
        cycle += 1

    return message_list