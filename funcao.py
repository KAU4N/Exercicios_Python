#def impreimir_dados(nome, idade):
#    print("nome: {}, idade: {}".format(nome, idade))

#impreimir_dados('kauan', 18)
#
#
#def somar_numeros(n1, n2):
#    soma = n1 + n2
#    return soma
#
#resultado = somar_numeros(9, 11)
#
#print(resultado)

#o *args permite que o usuario nao tenha limites de quantos itens possa colocar la.

def titulos_copa_mudo(pais, *args):
    print('o pais {}'.format(pais))
    print('ganhou a copa do mundo nos anos: ')
    for titulo in args:
        print(titulo)

titulos_copa_mudo('Brasil', '1990', '1994', '2002')
