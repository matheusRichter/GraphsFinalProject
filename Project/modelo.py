""" 
    Modelo de grafo que possue as capitais dos estado ligadas a todas as demais cidades
    dos estado e ligadas a capitais do demais estado. O peso das arestas é a distância
    entre as cidade.
"""
import csv
import threading
from multiprocessing import Process
from funções_extras import *

estados = {}
capitais = {}
tamanho = 0

# Lê trabcsv e tranforma em dicionario com estados e suas cidades
with open("cidades.csv",'r') as arquivo:
    texto = csv.reader(arquivo, delimiter=',')
    for row in texto:

        if row[1] == "cidade":
            continue
        if row[0].lower() not in estados:
            estados[row[0].lower()] = [row[1].lower()]
        else:
            estados[row[0].lower()].append(row[1].lower())
        tamanho += 1


# Lê us_state_capitals e tranforma em dicionario com estados e sua capitais
with open("capitais.csv",'r') as arquivo:
    capitals = csv.reader(arquivo, delimiter=',')
    for row in capitals:
        if row[1] == "cidade":
            continue
        capitais[row[0].lower()] = row[1].lower()


# Cria grafo com o tamanho igual ao numero de cidades

grafo = Grafo(tamanho)

# Cria vertices
cont = 0
for estado in estados:
    for cidade in estados[estado]:
        grafo.setInfo(cont, cidade)
        cont += 1

# Cria adjacencias entre cidades do mesmo estado
for capital in capitais:
    for cidade in estados[capital]:
        if capitais[capital] != cidade:
            grafo.criaAdjascencia(grafo.getIndex(capitais[capital]), grafo.getIndex(cidade), random.randint(1, 20))



# Cria adjacencias entre capitais
with open("fronteiras.csv",'r') as arquivo:
    texto = csv.reader(arquivo, delimiter=',')
    for row in texto:
        if row[1] != 'uf':
            grafo.criaAdjascencia(grafo.getIndex(capitais[row[0]]), grafo.getIndex(capitais[row[1]]), random.randint(1, 20))


# for estado in estados:
#     for i in range(len(estados[estado])*3):
#         grafo.criaAdjascencia(random.randint(grafo.getIndex(estados[estado][0]), grafo.getIndex(estados[estado][-1])),
#                               random.randint(0, 10))

print(grafo.numeroDeVertices())
print(grafo.numeroDeArestas())

if __name__ == '__main__':
    grafo.is_euleriano()