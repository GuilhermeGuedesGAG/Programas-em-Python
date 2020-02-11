'''
Este jogo usa a fórmula random/ou aleatório em Inglês
Segue abaixo as orientações para fazer este programa :
Boas Vindas!
Sistema sorteia um número
Sistemas solicita ao jogador seu palpite.
Se errou, informar se para maia ou para menos, solicitar outro palpite e informar
quantas tentativas ainda restam
Se acertou, parabenizar e informar o número de tentativas utilizadas.
Número máximo de tentativas = 7
'''

import random

chute = 0
chances = 7
tentativas = 1
jogador = ''
# Sistema sorteará un número entre 1 e 100
numero_secreto = random.randint(1, 100)

print('########################################################')
print('Bem vindo ao jogo de Adivinha')
print('Você terá sete chances para adivinhar o número')
print('##########################################################')

jogador = input('Digite seu nome:')  # Aqui o programa insere o nome do jogador
print('Chute um número entre 1 e 100 :')

while tentativas <= 7:  # loop com while(repetir,ou seja aqui vai repetir o tentivas)menores ou igual a 7 x o máximo
    chute = int(input('Digite o seu número :'))
    if chute < numero_secreto:
        print('Você errou. Seu número é menor do que o sorteado,'
              'tente novamente.)')
        print('Tentativa %d de %d' % (tentativas, chances))
    elif chute == numero_secreto:
        print('Parábens !!!!!', jogador)
        print('Você acertou com %d tentativas' % (tentativas))
        tentativas = 7
    else:
        print('Você errou,seu número é maior que o sorteado,'
              'tente novamente')
        print('Tentativa %d de %d' % (tentativas, chances))

        if tentativas == 6:
            print('Última tentativa')
        elif tentativas == 7:
            print("### Fim do Jogo")

        tentativas = tentativas + 1
