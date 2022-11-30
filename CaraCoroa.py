from random import randint

resultados = ('Cara', 'Coroa')
maquina = randint(0, 1)

print(''' 
=-=-=-=-=-=-=-=-=-=
| [0] Cara        |
| [1] Coroa       |
=-=-=-=-=-=-=-=-=-=
''')

jogador = int(input('Escolha sua jogada: '))
print('O Resultado foi: {}'.format(resultados[maquina]))
print('Você jogou: {}'.format(resultados[jogador]))

if maquina == 0:
    if jogador == 0:
        print('\033[1;32mVocê acertou!\033[m')
    else:
        print('\033[1;31mVocê errou\033[m')
elif maquina == 1:
    if jogador == 1:
        print('\033[1;32mVocê acertou!\033[m')
    else:
        print('\033[1;31mVocê errou\033[m')
