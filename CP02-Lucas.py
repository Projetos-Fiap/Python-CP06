catalogo = {
    'Vinho tinto': 50.00,
    'Vinho branco': 90.00,
    'Vinho rosé': 75.00,
    'Champagne': 110.00,
    'Espumante': 200.00,
}
estoque = ['Vinho tinto', 'Vinho branco', 'Vinho rosé', 'Champagne', 'Espumante']
estoqueQuantidade = []
estoqueCompleto = []
suprementos = []

menu = int(input('Qual menu você deseja entrar? \n 1.Estoque \n 2.Suprementos '))

if menu == 1:
    opcaoEstoque = int(input('Você deseja: \n 1.Adicionar um produto ao estoque \n 2.Retirar um produto do estoque \n 3.Adiciona-lo a lista de suprimentos para ser comprado \n 4.Ver estoque atual '))
    if opcaoEstoque == 1:
        for vinho, preco in catalogo.items(): 
            numeros = int(input(f'Quanto {vinho} adicona? '))
            estoqueQuantidade.append(numeros)
        estoqueCompleto = sum(zip(estoque, estoqueQuantidade), ())    
        print(f'Seu estoque atual é {estoqueCompleto}.')

    else:
        print('Você precisa digitar uma opção váalida.')    
elif menu == 2:
    for True in suprementos:
        

else:
    print('3')