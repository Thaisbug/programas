#Apliacando seus conhecimentos sobre laços de repetição
Quantidadeimpares = 0
QuantidadePares = 0
for i in range (5):
    numero = int(input("informe um numero: \n"))
    if numero % 2 == 0: #numero é par 
        QuantidadePares = QuantidadePares + 1
    else:
        Quantidadeimpares = Quantidadeimpares + 1
print (f"quantidade de pares: {QuantidadePares}")
print (f"quantidade de impares: {Quantidadeimpares}")