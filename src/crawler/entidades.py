import json
import re
from string import punctuation
from vaderSentimentPtbr.vaderSentiment import SentimentIntensityAnalyzer
from pymongo import MongoClient

from settings import *


NAO_ENTIDADES = {
    'Com', 'Ao', 'Em', 'No', 'Nesta', 'Com', 'Outro', 'Porém', 'Pelas', 'Isso', 'Percebe', 'Parte', 
    'Também', 'Após', 'Algo', 'Íntegra Leia', 'Pela', 'Foi', 'Será', 'Sei', 'Fiz', 'Vou', 'Leia',
    'Este', 'Estes', 'Esse', 'Esses', 'Houve', 'Seja', 'Sejam', 'Seriam', 'Serão', 'Têm', 'Tem',
    'Desse', 'Desses', 'Deste', 'Destes', 'Não', 'Sim', 'Sua', 'Seu', 'Fazr', 'São', 'Toda', 'Todo',
    'Existem', 'Termos', 'Devem', 'Fico', 'Talvez', 'Estamos', 'Porque', 'Ponto', 'Cerca', 'Nós',
    'Mudar', 'Duas', 'Uns', 'SAIBA COMO', 'Segundo', 'Segunda', 'Tempo', 'Festa', 'Hoje', 'Alto', 'Logo',
    'Estimativa', 'Ontem', 'Meus', 'Que', 'Júnior', 'Dessa', 'Desta', 'Atendimento', 'Cidade',
    'Aquele', 'Aquela', 'ENTENDA COMO', 'Completou', 'Esclareceu', 'Os', 'As', 'Na', 'No', 'Troco',
    'Garantimos', 'Insatisfeitos'
}

FRAGMENTO_TOKEN = {
    'Além', 'Para', 'Também', 'Disse', 'Saiba', 'Um', 'Uma', 'Completou', 'Segundo',

}

# Entidades compostas, com termos de inicial minúscula
ENTIDADES_COMPOSTAS = {
    'Rio de Janeiro', 'Mato Grosso do Sul', 'Rio Grande do Norte', 'Rio Grande do Sul',
    'Câmara dos Deputados', 'Conselho de Justiça Federal', 'Ministério da Agricultura',
    'Ministério da Ciência e Tecnologia', 'Ministério da Cultura', 'Ministério da Fazenda',
    'Ministério da Integração Nacional', 'Ministério da Justiça', 'Ministério das Comunicações',
    'Ministério das Relações Exteriores', 'Ministério do Desenvolvimento, Indústria e Comércio',
    'Luiz Inácio Lula da Silva', 'Portal da Saúde', 'Portal de Serviços e Informações',
    'Presidência da República', 'Procuradoria Geral da República', 'Superior Tribunal de Justiça',
    'Tribunal de Contas da União', 'Fundo de Investimentos', 'Justiça Federal'
}


class Entidades:
    def __init__(self, conector='»'):
        # Conector para entidades compostas
        self.conector = conector

    def parse(self, noticia):
        for e in ENTIDADES_COMPOSTAS:
            if e in noticia:
                noticia = noticia.replace(e, e.replace(' ', self.conector))

        txt = ''

        # Remove os espaços antes de . ! ?
        sem_espaco_pontos = re.sub(r'([\.!?]) +', r'\1', noticia)

        # Percorre os caracteres, deixando os inícios de frase em minúsculo
        for i, c in enumerate(sem_espaco_pontos):
            # Se for o primeiro caracter, ou precedido por . ! ?
            if i == 0 or (c.isupper() and sem_espaco_pontos[i - 1] in ['.', '!', '?', '“', '”', "'", '"']):
                txt += c.lower()
            else:
                txt += c

        # Converte pontuação em espacos
        sem_pontuacao = ''.join([c if c not in punctuation else ' ' for c in txt])

        # Remove espaços múltiplos
        txt = re.sub(r' +', ' ', sem_pontuacao)

        # Tokeniza
        tokens = txt.split(' ')

        # Junta tokens de entidade próximos. Ex.: Eike Batista
        tokens_2 = []

        _continue = False

        for i, t in enumerate(tokens):
            if _continue:
                _continue = False
                continue

            try:
                if t[0].isupper() and tokens[i + 1][0].isupper() and self.conector not in t + ' ' + tokens[i + 1]:
                    tokens_2.append(t + ' ' + tokens[i + 1])
                    _continue = True
                else:
                    tokens_2.append(t)
            except:
                pass

        # Entidades com inicial maiúscula
        entidades = [t.replace(self.conector, ' ') for t in tokens_2 if t[0].isupper() and len(t) > 1]

        entidades_ok = []

        # Evita que entidades separadas por pontuação fiquem juntas
        for j, e in enumerate(entidades):
            partes = e.split(' ')

            # Se ambas as partes ocorrem individualmente, remove a junção
            cont = 0
            for parte in partes:
                if parte in entidades:
                    cont += 1
            if len(partes) == 1 or cont < len(partes):
                entidades_ok.append(e)

        # Contagem de ocorrências das entidades
        cont_ent = [(entidades_ok.count(e), e) for e in entidades_ok]
        cont_ent.sort()

        entidades = {}
        for c, e in cont_ent:
            if e.strip('“”') in NAO_ENTIDADES:
                continue

            pula = False
            for p in e.split(' '):
                if len(p) <= 2:
                    pula = True
            if pula:
                continue

            # Remove, por exemplo, "Para Temer"
            e = ' '.join([x for x in e.split() if x not in FRAGMENTO_TOKEN])
            
            # String vazia
            if not e:
                continue

            # Dígitos na string
            if any(x in e for x in '0123456789'):
                continue

            entidades[e.strip('“”')] = c

        return entidades


# Analizadores de entidades e sentimentos
ent = Entidades()
analyzer = SentimentIntensityAnalyzer()


entidades = {}

def entidades_polarizadas(texto):
    '''
        Percorre o texto, sentença a sentença, e retorna todas 
        as entidades encontradas e a polaridade de cada uma.
    '''
    sentencas = re.split(r'[.,]', texto)

    # Filtra as sentenças
    sentencas = [x.replace('\n', ' ').strip('“”') for x in sentencas]
    sentencas = [x for x in sentencas if x and len(x.split(' ')) > 1]

    for s in sentencas:
        # Entidades da sentença
        ents = ent.parse(s)

        if ents:
            # Polaridade da sentença
            s_score = analyzer.polarity_scores(s)['compound']

            # Para cada entidade da sentença
            for e in ents:
                if e not in entidades:
                    entidades[e] = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}
                
                entidades[e]['count'] += 1
                if s_score >= 0.3:
                    entidades[e]['pos'] += 1
                elif s_score <= -0.3:
                    entidades[e]['neg'] += 1
                else:
                    entidades[e]['neu'] += 1

    return entidades



if __name__ == '__main__':
    noticia = '''
Cunha diz à Justiça que não recebeu dinheiro da JBS para ficar em silêncio

Irmãos Joesley e Wesley Batista disseram na delação que Temer deu aval para comprarem o silêncio do ex-deputado. Cunha disse ainda que passa por 'penúria' financeira.
-presidente da Câmara dos Deputados Eduardo Cunha (PMDB-RJ) disse nesta segunda-feira (5), em depoimento à Justiça Federal em Brasília, que não recebeu dinheiro da empresa JBS para ficar em silêncio.
Os irmãos Joesley e Wesley Batista, do grupo que controla a JBS, disseram ao Ministério Público que receberam o aval do presidente Michel Temer para comprar o silêncio do ex-deputado.
Em seu acordo de delação premiada, que está sob investigação, Joesley entregou o aúdio de uma conversa dele com Temer em que o presidente diz "tem que manter isso aí", após o empresário afirmar que está bem com Eduardo Cunha.
Segundo a denúncia apresentada pela Procuradoria Geral da República contra Temer por obstrução à Justiça, o presidente se referia à compra do silêncio de Cunha.
Cunha chamou a denúncia dos irmãos Batista de "forjada" e disse que foi uma tentativa de "pegar" o mandato de Temer.
“Não existe essa história de dizer que eu estou em silêncio ou que eu vendi o meu silêncio para não delatar. Eu atribuo isso [...] para justificar uma denúncia que pegasse o mandato do Michel Temer. Essa é que é a verdade. Deram uma forjada e o Joesley foi cúmplice dessa forjada”, afirmou Cunha.
A defesa do presidente da República também vem negando a denúncia, desde que a delação dos irmãos Batista se tornou pública.
Cunha disse que conheceu Joesley Batista bem antes do que o empresário afirma. O ex-deputado contou que foi apresentado ao dono da JBS pelo também delator Lúcio Funaro em 2011, e não em 2014, como afirmou o empresário.
“Eu comprovo várias relações e encontros com ele. E talvez tenha até mensagens”, declarou durante a audiência.

Cunha afirma que não recebeu dinheiro Eike Batista da JBS para ficar em silêncio
'Penúria' financeira
Preso desde outubro de 2016, Cunha disse que atualmente não possui nenhuma renda. Ele citou o bloqueio dos bens e disse que está passando dificuldades.
“Estou em absoluta penúria”, afirmou o ex-deputado. Ele se queixou das dificuldades para bancar os gastos com sua defesa, como o pagamento de honorários ao advogado e das passagens para eles se reunirem em Curitiba, onde ex-deputado está preso.
Cunha disse que, por esse motivo, a sua defesa tem sido cerceada e que a sua transferência temporária para Brasília para depor e acompanhar os interrogatórios dos demais réus tem facilitado o contato com seu advogado.
'Tudo é o Eduardo Cunha'
O ex-presidente da Câmara prestou depoimento em uma investigação sobre o suposto esquema de propinas envolvendo financiamentos do Fundo de Investimentos do FGTS (FI-FGTS), administrado pela Caixa Econômica Federal.
O esquema é investigado pela Operação Sépsis, um desdobramento da Lava Jato. Além de Cunha, também são réus nesse processo Lúcio Funaro, Fábio Cleto, ex-vice-presidente da Caixa, e Henrique Eduardo Alves, ex-ministro e ex-presidente da Câmara.
Cunha atacou Funaro logo no início do depoimento. O operador do PMDB, em audiência no fim de outubro, confirmou a existência do esquema de corrupção e listou políticos do partido que teriam se beneficiado, como Cunha e o presidente Michel Temer.
"A delação que ele [Funaro] faz agora está me transformando num posto Ipiranga. Tudo é Eduardo Cunha", disse o ex-presidente da Câmara.
Cunha refutou as acusações de corrupção e disse que irá contestar todas. "Nenhuma delas é verdadeira e eu quero rebater cada ponto delas", continuou Cunha.
Ao detalhar a sua relação com Funaro, Cunha disse que os dois se aproximaram em 2003, quando o operador fez doações para a campanha do ex-deputado.
A partir daí, contou que se tornaram amigos e começaram a operar juntos no mercado financeiro.
"O fato de ele [Funaro] dizer que não é doleiro, é só quebrar o sigilo. Essa muita movimentação é que vai mostrar que ele era doleiro", disse Cunha. "Isso é só para explicar que ele era doleiro, apesar de negar", completou.
Cunha relatou ainda diversas situações em que as informações políticas beneficiaram Funaro e ele nessas operações. "Eu tinha muito boas informações e ganhava na maioria. O Lúcio começou a entender que as informações que vinham de Brasília acabavam tendo repercussão no mercado financeiro", disse.
Por conta disso, segundo o ex-deputado, Funaro ficou interessado em disputar uma vaga como deputado por Pernambuco, mas cabou desistindo das suas pretensões eleitorais porque seu nome veio à tona no escândalo do mensalão.
Cunha negou que Funaro tenha relação com o PMDB e seja operador de propina do partido, conforme acusa o Ministério Público.
"Nenhuma [relação com o PMDB], zero, zero. Ninguém sabe quem é Lúcio Funaro. Operador nenhum, operador coisa nenhuma. É uma historia que ele está criando para ter uma delação. Todo mundo que ele conheceu foi através de mim", declarou o ex-deputado.

Em seu depoimento, Eduardo Cunha isentou Michel Temer de ter relação com Funaro.
"Lúcio Funaro nunca teve acesso ao Michel Temer", disse Cunha. Segundo o ex-deputado, as três ocasiões de encontro citadas por Funaro em sua delação não são verdadeiras.
Uma delas teria sido em um culto religioso em um templo, outra em um comício de campanha e a terceira na base aérea de São Paulo.
"O culto era em um lugar para 12 mil pessoas sentadas e não é qualquer um que entra no púlpito. O Temer estava no púlpito, o Lúcio não deve nem ter passado perto", disse.
E continuou: "É mentira. Só se houve outros momentos. Na minha frente, ele nunca cumprimentou o Michel Temer. Nessas três ocasiões, eu estava com Michel Temer".
Recusa em analisar assinatura
Durante a audiência, o representante do Ministério Público questionou Cunha sobre um papel entregue momentos antes pela defesa do doleiro Lúcio Funaro. O procurador queria saber se a assinatura que constava no documento era dele, mas o ex-deputado se recusou até mesmo a olhar o papel.
Ele alegou que só responderia depois que o documento fosse formalmente juntado ao processo e uma perícia, feita. “Faça o juntamento [aos autos], com a perícia comprovando que é minha a letra, e aí venha me questionar”, contestou Cunha.
Cunha negou que Funaro pagasse contas pessoais suas, mas admitiu que às vezes usava a estrutura do escritório dele, em São Paulo, para fazer pagamentos. Ele justificou que isso era necessário porque, quando estava na cidade, não tinha assessoria parlamentar como em Brasília ou no Rio de Janeiro.
“A nossa atividade deixa a gente muito desregrado com a nossa vida pessoal, às vezes pagava muita coisa atrasada”, disse.
'''

    # ent_pol = entidades_polarizadas(noticia)
    # for e in ent_pol:
    #     print(e, ent_pol[e])


    ### Calcula a polaridade de todas as entidades das notícias coletadas
    cliente = MongoClient(IP_BD, PORTA_BD)
    banco = cliente[NOME_BD]
    noticias = banco[COLECAO_BD]


    cont = 0
    for n in noticias.find():
        conteudo = n['conteudo']
        entidades_polarizadas(conteudo)
        cont += 1


    json.dump(entidades, open('entidades_polarizadas.json', 'w'))