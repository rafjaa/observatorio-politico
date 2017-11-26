import random
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date
from parallelpython import parallelize
from pymongo import MongoClient
import requests
from vaderSentimentPtbr.vaderSentiment import SentimentIntensityAnalyzer

import entidades
from settings import *


# Analizador de sentimentos
analyzer = SentimentIntensityAnalyzer()

# Analisador de entidades
ent = entidades.Entidades()


def parser_g1(soup):
    dados = {}

    dados['titulo'] = soup.find('h1', class_='content-head__title').text
    dados['postagem'] = soup.find('time')['datetime']
    dados['postagem'] = parse_date(dados['postagem'], fuzzy=True)

    dados['conteudo'] = '\n'.join([p.text for p in soup.find_all('p', class_='content-text__container')])

    return dados


def parser_g1_economia(soup):
    dados = {}    

    dados['titulo'] = soup.find('h1', class_='entry-title').text
    dados['postagem'] = soup.find('abbr', class_='published').text
    dados['postagem'] = parse_date(dados['postagem'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find_all('p'):
        if not p.has_attr('class') or p['class'][0] not in ['subtitulo', 'menu-submenu-title', 'vcard', 'menu-mosaic-title']:
            paragrafos_texto.append(p.text)

    dados['conteudo'] = '\n'.join(paragrafos_texto[1:])

    return dados


def parser_g1_politica_blog(soup):
    dados = {}  

    dados['titulo'] = soup.find('title').text.strip()
    dados['postagem'] = soup.find('time')['datetime']
    dados['postagem'] = parse_date(dados['postagem'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('section', class_='post-content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['conteudo'] = '\n'.join(paragrafos_texto)

    return dados


def parser_agencia_brasil(soup):
    dados = {}

    dados['titulo'] = soup.find('h1', class_='title').text.strip()
    dados['postagem'] = soup.find('li', class_='date').text.split('publica')[0]
    dados['postagem'] = parse_date(dados['postagem'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('div', class_='content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['conteudo'] = '\n'.join(paragrafos_texto)

    return dados


def parser_otempo(soup):
    dados = {}

    dados['titulo'] = soup.find('div', class_='titleNews').text.strip()
    dados['postagem'] = soup.find('div', class_='published-date').text.split('EM')[1].strip()
    dados['postagem'] = parse_date(dados['postagem'], fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('span', class_='texto-artigo').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['conteudo'] = '\n'.join(paragrafos_texto)

    return dados


def parser_politica_livre(soup):
    dados = {}

    dados['titulo'] = soup.find('title').text.split('|')[0].strip()
    partes_data = soup.find('p', class_='data').text.split(',')[1].strip().replace(' de ', '/').split('/')
    partes_data[1] = str(MESES[partes_data[1]])
    dados['postagem'] = parse_date('/'.join(partes_data), fuzzy=True)

    paragrafos_texto = []

    for p in soup.find('div', class_='entry-content').find_all('p'):
        paragrafos_texto.append(p.text)

    dados['conteudo'] = '\n'.join(paragrafos_texto)

    return dados


def parser_nominuto(soup):
    dados = {}

    dados['titulo'] = soup.find('h1', class_='title').text.strip()
    dados['postagem'] = soup.find('time', class_='date')['datetime'].split(' ')[0].replace('-', '/')

    dados['postagem'] = parse_date(dados['postagem'], fuzzy=True)

    paragrafos_texto = []

    sec_content = soup.find('section', class_='content')

    for p in sec_content.find_all('p'):
        paragrafos_texto.append(p.text)

    # Caso só haja um parágrafo, sem tag <p>
    if '<p' not in sec_content.text:
        paragrafos_texto.append(sec_content.text)

    dados['conteudo'] = '\n'.join(paragrafos_texto)

    return dados


def obtem_noticia(url):
    user_agent = random.choice(USER_AGENTS)
    html = requests.get(url, headers={'User-Agent': user_agent}).text

    for parser in [parser_g1, parser_g1_economia, parser_g1_politica_blog, parser_agencia_brasil, parser_otempo, parser_politica_livre, parser_nominuto]:
        try:
            json_noticia = parser(BeautifulSoup(html, 'html.parser'))

            json_noticia['url'] = url

            # Análise de sentimentos
            json_noticia['polaridade'] = analyzer.polarity_scores(json_noticia['conteudo'])
            json_noticia['entidades'] = ent.parse(json_noticia['conteudo'])

            return json_noticia
        except Exception as ex:
            pass

    # Caso não tenha conseguido processar o template
    return False


def persiste(json_noticia):
        cliente = MongoClient(IP_BD, PORTA_BD)
        banco = cliente[NOME_BD]
        noticias = banco[COLECAO_BD]

        obj_id = noticias.insert_one(json_noticia)
        cliente.close()

        return obj_id

    
# Percorre os links das notícias, baixando, processando e 
# persistindo paralelamente no MongoDB
def persiste_noticia(url):
    try:
        json_noticia = obtem_noticia(url)

        # Caso a notícia tenha sido processada corretamente
        if json_noticia:
            obj_id = persiste(json_noticia)
            print('Inserido:', obj_id)
        else:
            print('Erro: ', url)
    except:
        print('Erro inserção:', url)
        pass


if __name__ == '__main__':
    # Exibe as informações do BD
    cliente = MongoClient(IP_BD, PORTA_BD)
    banco = cliente[NOME_BD]
    noticias = banco[COLECAO_BD]

    print(noticias.count(), 'notícias persistidas')    

    links = [l.strip() for l in open(PASTA_LINKS + 'links_agencia_brasil.txt')]
    parallelize(persiste_noticia, links)