contador = 1
notas = []

while contador <= 4:
    nota = float(input('insira sua nota: '))
    notas.append(nota)
    contador = contador + 1


media = sum(notas) / 4


aprovado =  media > 7
if  aprovado:
    print('Parabens vc foi aprovado.')

recuperacao = media < 7 and media > 5.5

if recuperacao:
    print('vc esta de recuperacao')

reprovado = media < 5.5

if reprovado:
    print('vc foi reporvado')

print('sua média é: ', media)