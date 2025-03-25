produto = {
    'nome': 'Feijão',
    'quantidade': 10
    }

nome = produto ['nome']
quantidade = produto ['quantidade']
print ("nome :", nome)
print ('quantidade : ', quantidade)

#usando dicionario

produto = {
    'nome': 'Feijão',
    'quantidade': 10
    }

#Alterando o valor
produto ['quantidade'] = 100

nome = produto ['nome']
quantidade = produto ['quantidade']

print ("nome :", nome)
print ('quantidade : ', quantidade)



produto = {
    'nome': 'Feijão',
    'quantidade': 10
    }

for chave, valor in produto.items ():
    print(chave, valor)
    