#Equipe:
# Arthur Savio
# Guilherme Amaral
# Joao Victor Ribeiro
#Tabela 15

entrada = \
    [[1,1,1],
     [1,1,0],
     [1,0,1],
     [1,0,0],
     [0,1,1],
     [0,1,0],
     [0,0,1],
     [0,0,0]]
peso = [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
resposta_esperada=[1,1,1,1,1,1,0,1]

def funcao_degrau(soma):
    if soma < 0:
        saida = 0
    else:
        saida = 1
    return saida

def not_camada_5(matriz_resposta):
    soma = 0.0
    soma += matriz_resposta[0][3] * peso[8]

    # Funcao degrau
    return funcao_degrau(soma)

def or_and_camada_4(matriz_resposta):
    soma = 0.0
    soma += matriz_resposta[0][2] * peso[6]
    soma += matriz_resposta[2][0] * peso[7]

    # Funcao degrau
    return funcao_degrau(soma)

def not_camada_3(matriz_resposta):
    soma = 0.0
    soma += matriz_resposta[0][1] * peso[5]

    # Funcao degrau
    return funcao_degrau(soma)

def or_and_camada_2(matriz_resposta):
    soma = 0.0
    soma += matriz_resposta[0][0] * peso[3]
    soma += matriz_resposta[1][0] * peso[4]

    # Funcao degrau
    print("SOMA segunda camada: " + str(soma))
    return funcao_degrau(soma)

def not_camada_1(i,j):
    soma = 0.0
    soma += entrada[i][j] * peso[j]

    # Funcao degrau
    return funcao_degrau(soma)

def treinamento():
    epoca = 0
    while True:
        loop = True
        print ("EPOCA: "+ str(epoca))
        for i in range(len(entrada)):
            matriz_resposta = [[0,0,0,0,0],
                               [0],
                               [0]]
            #1 camada NOT
            for j in range(3):
                matriz_resposta[j][0] = not_camada_1(i,j)

            #2 Camada OR/AND
            matriz_resposta[0][1] = or_and_camada_2(matriz_resposta)

            #3 Camada NOT
            matriz_resposta[0][2] = not_camada_3(matriz_resposta)

            #3 camada OR/AND
            matriz_resposta[0][3] = or_and_camada_4(matriz_resposta)

            #4 camada NOT
            matriz_resposta[0][4] = not_camada_5(matriz_resposta)

            # print(matriz_resposta)
            erro = resposta_esperada[i] - matriz_resposta[0][4]

            print("ERROR: " + str(erro))
            if erro != 0:
                loop = False
                print("Entrada : " + str(entrada[i]))
                peso[0] = peso[0] + 0.1 * erro * entrada[i][0]
                peso[1] = peso[1] + 0.1 * erro * entrada[i][1]
                peso[2] = peso[2] + 0.1 * erro * entrada[i][2]
                peso[3] = peso[3] + 0.1 * erro * matriz_resposta[0][0]
                peso[4] = peso[4] + 0.1 * erro * matriz_resposta[1][0]
                peso[5] = peso[5] + 0.1 * erro * matriz_resposta[0][1]
                peso[6] = peso[6] + 0.1 * erro * matriz_resposta[0][2]
                peso[7] = peso[7] + 0.1 * erro * matriz_resposta[2][0]
                peso[8] = peso[8] + 0.1 * erro * matriz_resposta[0][3]
            print(matriz_resposta)
            print(peso)
        epoca += 1
        # print(peso)
        if loop:
            break;

if __name__ == '__main__':
    treinamento()
    # print(peso)
