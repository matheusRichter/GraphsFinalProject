import time

from MatrizEsparsa import*
from Node import*
import random

class Grafo:

    def __init__(self, tamanho:int):
        self.__tamanho = tamanho
        self.__nos = [None for i in range(self.__tamanho)]
        self.__matriz_adj = MatrizEsparsa(tamanho)

    # function to return number of vertecies
    def getSize(self): return self.__tamanho

    # functions that return list of edges
    def arestas(self): return self.__matriz_adj.lista_de_arestas()

    # function to link vertices
    def criaAdjascencia(self, vertice:int, lable:int, peso:float=1):
        self.__matriz_adj.setValue(vertice, lable, peso)

    # function to unlink vertices
    def removeAdjascencia(self, vertice:int, lable:int):
        self.__matriz_adj.removeValue(vertice, lable)

    # function to print matrix of adjacencies
    def imprimeAdjascencias(self):
        self.__matriz_adj.imprimir()

    # function to set node value in list __nos
    def setInfo(self,i:int,info:str):
        self.__nos[i] = Node(info)

    # function to count number of adjacencies of a vertices
    def adjacentes(self, i:int):
        return self.__matriz_adj.countEach(i)
    
    # function that returns name of nodes in _nos
    def getNodes(self):
        nodes = []
        for i in self.__nos:
            nodes.append(i.getNome())
        return nodes

    # get index
    def getIndex(self,nome):
        c = self.getNodes()
        return c.index(nome)

    # function that returns weight of an adjacencie
    def peso(self, i:int, j:int):
        return self.__matriz_adj.getPeso(i, j)

    def warshall(self):
        return self.__matriz_adj.warshall()

    def printWarshall(self, i=None, j=None):
        self.__matriz_adj.printWarshall(i, j)

    def dijkstra(self):
        return self.__matriz_adj.Dijkstra()

    def printDijkstra(self, i=None, j=None):
        return self.__matriz_adj.printDijkstra(i, j)

    def buscaLargura(self, fila:list, j:int):
        return self.__matriz_adj.largura(fila,j)

    def buscaProfundidade(self, origem:int, destino:int):
        return self.__matriz_adj.profundidade(origem, destino)

    def numeroDeVertices(self):
        return len(self.__nos)

    def maiorEntrada(self):
        return self.__matriz_adj.maiorEntrada()

    def maiorSaida(self):
        return self.__matriz_adj.maiorSaida()

    def maioresSaidas(self):
        return self.__matriz_adj.maioresSaidas()

    def maioresEntradas(self):
        return self.__matriz_adj.maioresEntradas()

    def numeroDeVertices(self):
        return self.__tamanho

    def numeroDeArestas(self):
        return self.__matriz_adj.count()

    def nArestasDistante(self, origem, distancia):
        return self.__matriz_adj.nArestasDistante(origem, distancia)

    def vertices_N_distante(self,s,d):
        return self.__matriz_adj.vertice_N_distante(s,d)

    def caminhoMaisLongo(self, origem, destino):
        return self.__matriz_adj.checkLongestPath(origem,destino)

    def caminhos(self, origem, destino):
        return self.__matriz_adj.todosOsCaminhos(origem, destino)

    def n_componentes(self):
        i = 0
        S = []
        while len(S) < self.__tamanho:
            Visitados = []
            inicial = random.randint(0,self.__tamanho-1)
            if inicial not in S:
                Visitados = self.buscaProfundidade(inicial, self.__tamanho-1)
                i += 1
                S.append(Visitados)
                print('Componente ' + str(i) + ' ' + str(Visitados))

    def isCyclic(self):
        print("verificando isCyclic...")
        result = self.__matriz_adj.isCyclic()
        print("isCyclic: " + str(result))
        return result

    def prim(self):
        self.__matriz_adj.primMST()
    
    def is_clique(self, vertices):
        return self.__matriz_adj.is_clique(vertices)

    def clique_maximal(self, clique):
        return self.__matriz_adj.clique_maximal(clique)

    def agrupamento_local(self, vertice):
        return self.__matriz_adj.agrupamento_local(vertice)

    def agrupamento_medio(self):
        return self.__matriz_adj.agrupamento_medio()

    def is_euleriano(self):
        print("verificando is_euleriano...")
        result = self.__matriz_adj.is_euleriano()
        print("is_euleriano: " + str(result))
        return result

    def is_conexo(self):
        print("verificando is_conexo...")
        result = self.__matriz_adj.is_conexo()
        print("is_conexo: " + str(result))
        return result

    def centralidade_de_posicionamento(self, vertice):
        return self.__matriz_adj.centralidade_de_posicionamento(vertice)

    def centralidade_de_intermediacao(self, vertice):
        return self.__matriz_adj.centralidade_de_intermediacao(vertice)


if __name__ == '__main__':
    um = Grafo(3)

    um.setInfo(0, "zero")
    um.setInfo(1, "um")
    um.setInfo(2, "dois")

    um.criaAdjascencia(0,1,2)
    um.criaAdjascencia(0,2,1)
    um.criaAdjascencia(1,2,4)
    um.criaAdjascencia(2,0,5)

    print(um.centralidade_de_intermediacao(0))
    print(um.centralidade_de_posicionamento(0))
    um.isCyclic()
    um.is_euleriano()
    um.is_conexo()
