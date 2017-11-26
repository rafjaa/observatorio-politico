import random
import re

from dateutil.parser import parse as parse_date
from bs4 import BeautifulSoup
import requests

from settings import *


def parser_g1(soup):
    dados = {}

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('h1', class_='content-head__title').text
    dados['data'] = soup.find('time')['datetime']
    dados['data'] = parse_date(dados['data'], fuzzy=True)

    dados['texto'] = '\n'.join([p.text for p in soup.find_all('p', class_='content-text__container')])

    return dados


def parser_g1_economia(soup):
    dados = {}    

    dados['url'] = soup.find('div', class_='share-bar')['data-url']
    dados['titulo'] = soup.find('h1', class_='entry-title').text
    dados['data'] = soup.find('abbr', class_='published').text
    dados['data'] = parse_date(dados['data'], fuzzy=True)

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
    dados['data'] = parse_date(dados['data'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('section', class_='post-content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['texto'] = '\n'.join(paragrafos_texto)

    return dados


def parser_agencia_brasil(soup):
    dados = {}

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('h1', class_='title').text.strip()
    dados['data'] = soup.find('li', class_='date').text.split('publica')[0]
    dados['data'] = parse_date(dados['data'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('div', class_='content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['texto'] = '\n'.join(paragrafos_texto)

    return dados


def parser_otempo(soup):
    dados = {}

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('div', class_='titleNews').text.strip()
    dados['data'] = soup.find('div', class_='published-date').text.split('EM')[1].strip()
    dados['data'] = parse_date(dados['data'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('span', class_='texto-artigo').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['texto'] = '\n'.join(paragrafos_texto)

    return dados


def parser_politica_livre(soup):
    dados = {}

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('title').text.split('|')[0].strip()
    partes_data = soup.find('p', class_='data').text.split(',')[1].strip().replace(' de ', '/').split('/')
    partes_data[1] = str(MESES[partes_data[1]])
    dados['data'] = parse_date('/'.join(partes_data), fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('div', class_='entry-content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['texto'] = '\n'.join(paragrafos_texto)

    return dados


def parser_nominuto(soup):
    dados = {}

    dados['url'] = soup.find('link', rel='canonical')['href']
    dados['titulo'] = soup.find('h1', class_='title').text.strip()
    dados['data'] = soup.find('time', class_='date')['datetime'].split(' ')[0].replace('-', '/')

    dados['data'] = parse_date(dados['data'], fuzzy=True)

    paragrafos_texto = []

    sec_content = soup.find('section', class_='content')

    for p in sec_content.find_all('p'):
        paragrafos_texto.append(p.text)

    # Caso só haja um parágrafo, sem tag <p>
    if '<p' not in sec_content.text:
        paragrafos_texto.append(sec_content.text)

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
    
    # print(obtem_noticia(
    #     'https://g1.globo.com/economia/blog/joao-borges/post/meirelles-agora-ve-possibilidades-concretas-de-aprovacao-da-reforma-da-previdencia.ghtml',
    #     parser_g1
    #     ))

    # print(obtem_noticia(
    #     'http://agenciabrasil.ebc.com.br/politica/noticia/2017-11/temer-da-posse-baldy-e-fala-em-parceria-entre-governo-e-congresso',
    #     parser_agencia_brasil
    #     ))

    # print(obtem_noticia(
    #     'http://www.otempo.com.br//capa/pol%C3%ADtica/trf2-decide-que-adriana-ancelmo-deve-voltar-para-pris%C3%A3o-1.1545559',
    #     parser_otempo
    #     ))

    # print(obtem_noticia(
    #     'http://www.politicalivre.com.br/2017/05/termina-em-brasilia-maior-manifestacao-contra-governo-temer/',
    #     parser_politica_livre
    #     ))
    
    # print(obtem_noticia(
    #     'http://www.nominuto.com//noticias/politica/trf-2-diz-que-liberacao-de-deputados-precisa-de-aval-de-desembargador/162723/',
    #     parser_nominuto
    #     ))

    pass