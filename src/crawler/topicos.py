'''
    Aplica topic modeling para extrair os principais tópicos (assuntos) 
    dos documentos (notícias) coletados.
'''

import random
import nltk
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF
from pymongo import MongoClient
from settings import *


cliente = MongoClient(IP_BD, PORTA_BD)
banco = cliente[NOME_BD]
noticias = banco[COLECAO_BD]

stopwords = nltk.corpus.stopwords.words('portuguese')

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

# Número de tópicos
num_topics = 5

# Fatoração da Matriz Não-Negativa (NMF)
nmf_model = NMF(n_components=num_topics, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Matriz de tópicos x documentos (W)
nmf_W = nmf_model.transform(tfidf)

# Matriz de paralvras x tópicos (H)
nmf_H = nmf_model.components_

# Dimensão das matrizes resultantes
print('Matriz W:', nmf_W.shape)
print('Matriz H:', nmf_H.shape, '\n')


def exibe_topicos(H, W, feature_names, documents, num_top_words):
    for topic_idx, topic in enumerate(H):
        print('\nTópico %d' % (topic_idx + 1))

        print('   Principais termos: ' + ', '.join([feature_names[i] + ' (%s)' % round(H[topic_idx][i], 2) 
                            for i in topic.argsort()[:-num_top_words - 1:-1]]))       



# Número de palavras mais relacionadas que serão exibidas para cada tópico
num_top_words = 5

exibe_topicos(nmf_H, nmf_W, tfidf_feature_names, documentos, num_top_words)