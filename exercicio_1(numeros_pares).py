#1 entre com um numero e imprima se ele é par ou impar

numero = int(input('entre com um numero inteiro: '))

if numero % 2 == 0:
    print('o número' , numero, 'é par')
else:
    print('O número' , numero, 'é impar')