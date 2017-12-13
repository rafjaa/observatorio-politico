'''
    Aplica topic modeling para extrair os principais tópicos (assuntos) 
    dos documentos (notícias) coletados.

    Retorno:

    {
        "2": [
            [["termo1_t1", peso], ["termo2_t1", peso2], ["termo3_t1", peso3]],
            [["termo1_t2", peso4], ["termo2_t2", peso5], ["termo3_t2", peso6]],
        ]
    }
'''

import json
import random
import nltk
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
from pymongo import MongoClient
from settings import *

# Faixa de tópicos
FAIXA_TOPICOS = [2, 15]
FAIXA_TOPICOS[1] += 1

# Quantidade de termos principais por tópico
NUM_TOP_WORDS = 5

cliente = MongoClient(IP_BD, PORTA_BD)
banco = cliente[NOME_BD]
noticias = banco[COLECAO_BD]

stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords += ['ex', 'disse', ]

# Converte os documentos em lista de strings e embaralha
documentos = []
for i, n in enumerate(noticias.find()):
    doc = str(i) + '\n'
    doc += ' '.join([t for t in n['conteudo'].split(' ') if t not in stopwords])
    documentos.append(doc)

random.shuffle(documentos)

# Cria a matriz de features TF-IDF
tfidf_vectorizer = TfidfVectorizer(
    max_features=10000, # Máximo de tokens utilizados
)
tfidf = tfidf_vectorizer.fit_transform(documentos)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()


topicos = {}

# Itera pela faixa de tópicos que serão precomputados
for num_topics in range(*FAIXA_TOPICOS):

    print(num_topics, 'tópicos de 15')

    topicos[str(num_topics)] = []

    # Fatoração da Matriz Não-Negativa (NMF)
    nmf_model = NMF(n_components=num_topics, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

    # Matriz de tópicos x documentos (W)
    nmf_W = nmf_model.transform(tfidf)

    # Matriz de paralvras x tópicos (H)
    nmf_H = nmf_model.components_  

    for topic_idx, topic in enumerate(nmf_H):
        topicos[str(num_topics)].append([(tfidf_feature_names[i], round(nmf_H[topic_idx][i], 2)) 
            for i in topic.argsort()[:-NUM_TOP_WORDS - 1:-1]])


json.dump(topicos, open('faixa_topicos.json', 'w'))