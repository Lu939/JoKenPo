from random import randint
from time import sleep
vitjog = vitcom = 0
while True:
    itens = {1: 'pedra', 2: 'papel', 3: 'tesoura'}
    computador = randint(1, 3)
    jogador = int(input('Escolha um dos itens; [1] pedra, [2] papel, [3] tesoura, [4] sair:'))
    if jogador == 4:
        break
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)
    if jogador == 1 and computador == 1 or jogador == 2 and computador == 2 or jogador == 3 and computador == 3:
        print('EMPATOU!')
    elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
        print('JOGADOR VENCEU!')
        vitjog += 1
    elif jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
        print('COMPUTDOR VENCEU!')
        vitcom += 1
    print(f' jogador jogou {itens[jogador]} e o computador jogou {itens[computador]}')
if vitjog > vitcom:
    print('JOGADOR FOI O CAMPEÃO!')
elif vitjog == vitcom:
    print('TERMINARAM EMPATADOS')
else:
    print('COMPUTADOR FOI O CAMPEÃO!')
print(f' foram {vitjog} vitórias para o jogador {vitcom} vitórias para o computador!')