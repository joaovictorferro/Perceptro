entrada = \
    [[1,1,1],
     [1,1,0],
     [1,0,1],
     [1,0,0],
     [0,1,1],
     [0,1,0],
     [0,0,1],
     [0,0,0]]
peso = [0.3,0.3,0.3]
resposta_esperada=[1,1,1,1,1,1,0,1]

def pergunta():
    soma = 0.0
    variavel = []
    variavel.append(float(input("Digite o valor de q1\n")))
    variavel.append(float(input("Digite o valor de q2\n")))
    variavel.append(float(input("Digite o valor de q1\n")))

    for j in range(len(peso)):
        # print(Entrada[i])
        soma += peso[j] * variavel[j]
    # Funcao degrau
    if soma < 0:
        saida = 0
    else:
        saida = 1

    print("A resposta obtida foi " + str(saida))


def treinamento():
    loop = True
    while loop == True:
        for i in range(len(entrada)):
            soma = 0.0
            for j in range(len(peso)):
                #print(Entrada[i])
                soma += entrada[i][j] * peso[j]

            #Funcao degrau
            if soma < 0:
                saida = 0
            else:
                saida = 1

            erro = resposta_esperada[i] - saida

            if erro != 0:
                loop = loop and False
                for r in range(len(peso)):
                    peso[r] = peso[r] + 0.1 * (erro * entrada[i][r])
            else:
                loop = loop and True

if __name__ == '__main__':
    treinamento()
    print(peso)
    pergunta()