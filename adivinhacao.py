import random

def jogar():
    print('bem vindo ao jogo de adivinhação')
    numero_secreto = random.randrange(1,101)
    tota_de_tentativas = 0
    rodada = 176
    pontos = 1000

    print(numero_secreto)

    print('Qual nível de dificuldade você deseja?')
    print('(1) Fácil. (2) Médio, (3) Difícil')

    nivel = int(input('Defina o nível: '))


    if (nivel > 3):
            print('Você deve escolher apenas entre 1, 2 e 3')
    elif(nivel < 0):
            print('Você deve escolher apenas entre 1,2 e 3')
    else:


        if (nivel == 1):
            tota_de_tentativas = tota_de_tentativas + 20
        elif (nivel == 2):
            tota_de_tentativas = tota_de_tentativas + 10
        else:
            tota_de_tentativas = tota_de_tentativas + 5

    for rodada in range (1,tota_de_tentativas + 1):
        print('tentativa {} de {}: '.format(rodada , tota_de_tentativas))
        chute_str = input("Digite seu numero entre 1 e 100: ")
        print('Voce digitou ',chute_str)
        
        chute = int(chute_str)

        acertou = chute == numero_secreto

        maior = chute > numero_secreto

        menor = chute < numero_secreto

        if (chute > 100):
            print('Seu número é maior que 100, digite um numero entre 1 e 100')
            continue
        elif (chute < 1):
            print('Seu número é menor que 1, digite um número entre 1 e 100') 
            continue
            
        if (acertou):
                print('Voce acertou o número correto é {}!!!'.format(numero_secreto))
                break
        else:
                if(maior):
                    print('voce errou, seu chute foi maior que o numero secreto')
                elif(menor):
                    print('voce errou, seu chute foi menor do que o numero secreto')
                    pontos_perdidos = abs(numero_secreto - chute) 
                    pontos = pontos - pontos_perdidos

        print(pontos)


    #### print('teste de {1} de {0}'.format(rodada, numero_secreto)) <--- Funciona só com string ou float
    #### ('R$ {:1f}').format(1.59)
    #### 'R$ 1.590000'
    #### ('R$ {:.1f}').format(1.59)
    #### 'R$ 1.6'
    #### ('R$ {:.3f}').format(1.59)
    #### 'R$ 1.590'

if(__name__ == '__main__'):
     jogar()