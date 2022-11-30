from random import randint

jogadas = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('''
\033[1m===================\033[m
Opções de jogadas: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
\033[1m===================\033[m
''')
jogador = int(input('\033[1mSua jogada: '))
print('\033[1m~~\033[m'*12)
print('\033[1;35mA Máquina jogou {}'.format(jogadas[maquina]))
print('\033[1;36mO Jogador jogou {}\033[m'.format(jogadas[jogador]))
print('\033[1m~~\033[m'*12)

#Máquina jogou Pedra
if maquina == 0:
    if jogador == 0:
        print('\033[1;34mEMPATE!')

    elif jogador == 1:
        print('\033[1;32mJogador VENCEU!')
    
    elif jogador == 2:
        print('\033[1;31mMáquina VENCEU!')
    
    else:
        ('\033[1;33mJogada inválida, escolha uma das suas opções de jogadas!')
#Máquina jogou Papel
elif maquina == 1:
    if jogador == 0:
        print('\033[1;31mMáquina VENCEU!')

    elif jogador == 1:
        print('\033[1;34mEMPATE!')
    
    elif jogador == 2:
        print('\033[1;32mJogador VENCEU!')
    
    else:
        ('\033[1;33mJogada inválida, escolha uma das suas opções de jogadas!')
#Máquina jogou Tesoura
elif maquina == 2:
    if jogador == 0:
        print('\033[1;32mJogador VENCEU!')

    elif jogador == 1:
        print('\033[1;31mMáquina VENCEU!')
    
    elif jogador == 2:
        print('\033[1;34mEMPATE!')
    
    else:
        ('\033[1;33mJogada inválida, escolha uma das suas opções de jogadas!')