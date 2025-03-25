produto = {
    'Nome': ['Feijão', 'Farinha', 'Arroz'],
    'Quantidade': [10, 10, 100]
    }

for nome, quantidade in zip (produto ['Nome'], produto ['Quantidade']):
    print ("produto:", nome, "Quantidade : ", quantidade)


produto = {
    'Nome': ['Feijão', 'Farinha', 'Arroz'],
    'Quantidade': [10, 10, 100],
    'preço': [30,50, 100],
    }
for nome, quantidade, preço in zip (produto ['Nome'], produto ['Quantidade'], produto ['preço']):
    print ("produto:", nome, "\nQuantidade : ", quantidade, "\npreço", preço)

    