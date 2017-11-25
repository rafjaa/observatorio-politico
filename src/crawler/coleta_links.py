''' coleta_links.py

    Coleta os links das notícias.
'''

import random

from bs4 import BeautifulSoup
import requests

from settings import *


def parser_g1(soup):
    links = [a['href'] for a in soup.find_all('a', class_='feed-post-link')]
    
    return links


def parser_agencia_brasil(soup):
    links = ['http://agenciabrasil.ebc.com.br' + div.find('a')['href'] for div in soup.find_all('div', class_='titulo-noticia')]

    return links


def parser_otempo(soup):
    links = ['http://www.otempo.com.br/' + h2.find('a')['href'] for h2 in soup.find_all('h2')]

    return links


def parser_politica_livre(soup):
    links = [h1.find('a')['href'] for h1 in soup.find_all('h1', class_='entry-title')]

    return links


def parser_nominuto(soup):    
    links = ['http://www.nominuto.com/' + div.find('a')['href'] for div in soup.find('ul', class_='list').find_all('div', class_='link')]

    return links


def coleta(url, parser):
    '''
        Recebe a url com as notícias e o parser
        adequado para extrair os links das mesmas.
    '''
    user_agent = random.choice(USER_AGENTS)
    html = requests.get(url, headers={'User-Agent': user_agent}).text

    soup = BeautifulSoup(html, 'html.parser')
    
    return parser(soup)


def crawler(id_inicio, id_fim, url_navegacao, parser, nome_txt):
    links = []

    # Percorre as páginas de notícias obtendo o link de cada uma
    for i in range(id_inicio, id_fim + 1):
        print('Página', i)
        
        try:
            coletados = coleta(url_navegacao % i, parser)
            print(' - ', len(coletados), 'links coletados')

            links += coletados
        except:
            print('Erro na coleta: pulando página')

    f = open(PASTA_LINKS + nome_txt, 'w')
    f.write('\n'.join(links))
    f.close()


if __name__ == '__main__':
    # Coleta G1
    #crawler(1, 1000, 'http://g1.globo.com/politica/index/feed/pagina-%s.html', parser_g1, 'links_g1.txt')

    # Coleta Agência Brasil
    # crawler(1, 500, 'http://agenciabrasil.ebc.com.br/politica?page=%s', parser_agencia_brasil, 'links_agencia_brasil.txt')

    # Coleta O Tempo Política
    # crawler(1, 200, 'http://www.otempo.com.br/capa/pol%%C3%%ADtica/%%C3%%BAltimas?page=%s', parser_otempo, 'links_otempo.txt')

    # Coleta Política Livre
    # crawler(1, 500, 'http://www.politicalivre.com.br/category/brasil/page/%s/', parser_politica_livre, 'links_politica_livre.txt')

    # Coleta NoMinuto
    # crawler(1, 500, 'http://www.nominuto.com/noticias/politica/?page=%s', parser_nominuto, 'links_nominuto.txt')
    
    pass