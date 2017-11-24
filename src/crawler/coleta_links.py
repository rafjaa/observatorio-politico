''' coleta_links.py

    Coleta os links das notícias.
'''

import random

from bs4 import BeautifulSoup
import requests


PASTA_LINKS = './links/'

# Agentes de usuário, via http://useragentstring.com/pages/useragentstring.php
USER_AGENTS = [
    # Chrome
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',

    # FireFox
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Android; U; Android; pl; rv:1.9.2.8) Gecko/20100202 Firefox/3.5.8',
    'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',

    # IE / Edge
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',

    # Safari
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',

    # Opera
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',

    # RockMelt
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24'
]


def parser_g1(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', class_='feed-post-link')]
    
    return links


def parser_agencia_brasil(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = ['http://agenciabrasil.ebc.com.br' + div.find('a')['href'] for div in soup.find_all('div', class_='titulo-noticia')]

    return links


def parser_otempo(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = ['http://www.otempo.com.br/' + h2.find('a')['href'] for h2 in soup.find_all('h2')]

    return links


def parser_politica_livre(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = [h1.find('a')['href'] for h1 in soup.find_all('h1', class_='entry-title')]

    return links


def parser_nominuto(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = ['http://www.nominuto.com/' + div.find('a')['href'] for div in soup.find('ul', class_='list').find_all('div', class_='link')]

    return links


def coleta(url, parser):
    '''
        Recebe a url com as notícias e o parser
        adequado para extrair os links das mesmas.
    '''
    user_agent = random.choice(USER_AGENTS)
    html = requests.get(url, headers={'User-Agent': user_agent}).text
    
    return parser(html)


def crawler(id_inicio, id_fim, url_navegacao, parser, nome_txt):
    links = []

    # Percorre as páginas de notícias obtendo o link de cada uma
    for i in range(id_inicio, id_fim + 1):
        print('Página', i)
        
        coletados = coleta(url_navegacao % i, parser)
        print(' - ', len(coletados), 'links coletados')

        links += coletados

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