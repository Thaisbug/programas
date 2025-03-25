#adicionando um elemento da lista polo índice
amigos = []
amigos.append ("Amanda")
amigos.append ("Bia")
amigos.append ("Fanny")
amigos.append ("Marcos")
amigos.append ("Rosa")
amigos.append ("Fernada")
amigos.append ("Nazare")
amigos.append ("Felipe")
print ("lista de amigos : ", amigos)

#ordenando a lista
print ("lisa de amigos :", amigos)
amigos.sort ()
print("lista de amigos ordenada :", amigos)

#criando uma lista
lista = [25, 12, 21, 2, 40, 50, 35]
lista.sort (reverse=True)
print (lista)
#imprimindo o maior elemento
maiorElemento = max (lista)
print ("maior elemento da lista : ", maiorElemento)
#adicionado um novo elemento
lista = [25, 12, 21, 2, 40, 50, 35]
lista.append (100)
lista.sort()
print(lista)
menorElemento = min(lista)
print("menorElemento:", menorElemento)

lista = [25, 12, 21, 2, 40, 50, 35]
lista.append (100)
lista.append (30)
lista.append (60)
lista.append (10)
lista.append (75)
lista.sort()
print(lista)
print("item: ",lista[4])
menorElemento = min(lista)
print("menorElemento:", menorElemento)


