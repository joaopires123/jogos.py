import forca
import adivinhacao

print('Qual jogo você quer jogar? (1) para adivinhação e (2) para forca')
jogo = int(input('Escolha seu jogo: '))

if(jogo == 1):
    print('Voce escolheu o jogo de adivinhação')
    adivinhacao.jogar()
elif(jogo == 2):
    print('Voce escolheu o jogo da forca')
    forca.jogar()
