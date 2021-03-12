from funções_extras import*

um = Grafo(3)

um.setInfo(0, "zero")
um.setInfo(1, "um")
um.setInfo(2, "dois")

um.criaAdjascencia(0,1,2)
um.criaAdjascencia(0,2,1)
um.criaAdjascencia(1,2,4)
um.criaAdjascencia(2,0,5)

print(um.is_conexo())
um.imprimeAdjascencias()
