import random

from bs4 import BeautifulSoup
import requests

from settings import *


def parser_g1(soup):
    return soup


def obtem_noticia(url, parser):
    user_agent = random.choice(USER_AGENTS)
    html = requests.get(url, headers={'User-Agent': user_agent}).text
    return parser(BeautifulSoup(html, 'html.parser'))



if __name__ == '__main__':
    print(obtem_noticia(
        'https://g1.globo.com/pr/parana/noticia/publicitario-diz-que-fez-repasses-de-propina-para-ex-presidente-da-petrobras-a-pedido-da-odebrecht.ghtml',
        parser_g1
        ))