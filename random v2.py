from random import randint  
computador = randint(0,100)
print('Sou seu computador :D e acabei de pensar em um número entre 0 e 100.')
print('Será que consegues adivinhar qual foi esse número?')
acertou = False
palpites = 0
while not acertou: 
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador: 
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente denovo.')
        elif jogador > computador: 
            print('Menos... Tente denovo.')
print('Acertou com {} tentativas. Parabéns!  (•◡•) /'.format(palpites))


