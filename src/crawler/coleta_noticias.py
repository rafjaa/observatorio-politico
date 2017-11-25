import random
import re

from bs4 import BeautifulSoup
import requests

from settings import *


def parser_g1(soup):
    dados = {}

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('h1', class_='content-head__title').text
    dados['data'] = soup.find('time')['datetime']
    dados['texto'] = '\n'.join([p.text for p in soup.find_all('p', class_='content-text__container')])

    return dados


def parser_g1_economia(soup):
    dados = {}    

    dados['url'] = soup.find('div', class_='share-bar')['data-url']
    dados['titulo'] = soup.find('h1', class_='entry-title').text
    dados['data'] = soup.find('abbr', class_='published').text

    paragrafos_texto = []

    for p in soup.find_all('p'):
        if not p.has_attr('class') or p['class'][0] not in ['subtitulo', 'menu-submenu-title', 'vcard', 'menu-mosaic-title']:
            paragrafos_texto.append(p.text)

    dados['texto'] = '\n'.join(paragrafos_texto[1:])

    return dados


def parser_g1_politica_blog(soup):
    dados = {}  

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('title').text.strip()
    dados['data'] = soup.find('time')['datetime']

    paragrafos_texto = []

    for p in soup.find('section', class_='post-content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['texto'] = '\n'.join(paragrafos_texto)

    return dados


def obtem_noticia(url, parser):
    user_agent = random.choice(USER_AGENTS)
    html = requests.get(url, headers={'User-Agent': user_agent}).text
    return parser(BeautifulSoup(html, 'html.parser'))



if __name__ == '__main__':
    # print(obtem_noticia(
    #     'https://g1.globo.com/pr/parana/noticia/publicitario-diz-que-fez-repasses-de-propina-para-ex-presidente-da-petrobras-a-pedido-da-odebrecht.ghtml',
    #     parser_g1
    #     ))

    # print(obtem_noticia(
    #     'http://g1.globo.com/economia/noticia/2016/10/governo-ressarcira-estados-em-r-19-bilhao-por-perdas-com-exportacoes.html',
    #     parser_g1_economia
    #     ))

    # print(obtem_noticia(
    #     'http://g1.globo.com/politica/blog/matheus-leitao/post/delator-diz-que-pagou-propina-luiz-sergio-na-cpi-da-petrobras.html',
    #     parser_g1_politica_blog
    #     ))

    # print(obtem_noticia(
    #     'http://g1.globo.com/politica/noticia/2016/10/em-5-meses-de-governo-temer-recebe-quase-14-do-congresso.html',
    #     parser_g1_economia
    #     ))
    
    print(obtem_noticia(
        'https://g1.globo.com/economia/blog/joao-borges/post/meirelles-agora-ve-possibilidades-concretas-de-aprovacao-da-reforma-da-previdencia.ghtml',
        parser_g1
        ))

    
    