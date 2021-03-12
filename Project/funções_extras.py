from Grafo import*

def gravar(grafo:Grafo, nome):
    print("Gravando...")
    g_file = open(f'{nome}.txt', 'w')
    
    # writing file
    # writing vertices
    g_file.write(f"* Vertices {grafo.getSize()}\n")
    for i in range(len(grafo.getNodes())):
        g_file.write(f'{i} "{grafo.getNodes()[i]}"\n')

    # writing edges
    g_file.write(f'* Arcs\n')
    for i in grafo.arestas():
        g_file.write(f'{i}\n')

    g_file.close()
    print("Gravado")

def recuperar(file:str):
    g_file = open(file, 'r')

    data = g_file.read()
    linhas = data.split('\n')

    grafo = Grafo(int(linhas[0][11:]))
    
    linha = 1
    for i in linhas[1:]:
        if i[0] == '*': break
        else:
            l = i.split() 
            grafo.setInfo(int(l[0]), l[1] + l[2])
        linha += 1

    for i in linhas[linha+1:-1]:
        l = i.split()
        grafo.criaAdjascencia(int(l[0]), int(l[1]), int(l[2]))

    return grafo

def adjcencias_conexas(grafo, vertice, vertices, v):
    if len(vertices) == 0:
        grafo.criaAdjascencia(vertice, v, random.randint(0, 10))
        return
    vertice2 = vertices.pop(random.randint(0,len(vertices)-1))
    grafo.criaAdjascencia(vertice, vertice2, random.randint(0, 10))
    adjcencias_conexas(grafo, vertice2, vertices, v)

def grafo_aleatorio(n_vertices=5, n_arestas=5, is_conexo=True):
    # erro se não for possível gerar grafo conexo
    if n_arestas < n_vertices and is_conexo == True:
        raise Exception('Não é possível gerar um grafo conexo com n_arestas menor que n_vertices')

    # criação de um novo grafo
    aleatorio = Grafo(n_vertices)

    # criação dos vértices
    for i in range(n_vertices):
        aleatorio.setInfo(i, f'Vertice {i}')

    # criação das adjacencias
    if is_conexo:
        vertices = [i for i in range(n_vertices)] # lista de vértices não usados
        v = vertices.pop(random.randint(0,len(vertices)-1)) # primeiro vértice usado
        adjcencias_conexas(aleatorio, v, vertices, v) # criação das adjacencias

        for i in range(n_arestas - len(aleatorio.arestas())):
            aleatorio.criaAdjascencia(random.randint(0, n_vertices-1), random.randint(0, n_vertices-1), random.randint(0,10))
    else:
        for i in range(n_arestas):
            aleatorio.criaAdjascencia(random.randint(0, n_vertices-1), random.randint(0, n_vertices-1), random.randint(0,10))

    return aleatorio

        
if __name__ == '__main__':
    um = grafo_aleatorio(5,8, False)
    um.imprimeAdjascencias()
    print(um.is_conexo())

    gravar(um, 'teste')
    print()

    dois = recuperar('teste.txt')
    dois.imprimeAdjascencias()
    print(dois.isCyclic())
    print(um.is_euleriano())