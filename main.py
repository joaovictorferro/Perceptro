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
peso = [0.3,0.3,0.3]
resposta_esperada=[1,1,1,1,1,1,0,1]

def pergunta():
    soma = 0.0
    variavel = []
    variavel.append(float(input("Digite o valor de q1\n")))
    variavel.append(float(input("Digite o valor de q2\n")))
    variavel.append(float(input("Digite o valor de q3\n")))

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
    cont = 0
    while True:
        loop = True
        print ("EPOCA: "+ str(cont))
        for i in range(len(entrada)):
            soma = 0.0
            for j in range(len(peso)):
                #print(Entrada[i])
                soma += entrada[i][j] * peso[j]
            print("SOMA: " + str(soma))
            #Funcao degrau
            if soma < 0:
                saida = 0
            else:
                saida = 1

            erro = resposta_esperada[i] - saida

            print("ERROR: " + str(erro))
            if erro != 0:
                loop = False
                for r in range(len(peso)):
                    peso[r] = peso[r] + 0.1 * (erro * entrada[i][r])
        cont += 1
        if loop:
            break;

if __name__ == '__main__':
    treinamento()
    print(peso)
    pergunta()