"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Rafael Agra de Castro Motta
  NUSP : 11807192
  Turma: 07
  Prof.: Andre Fujita

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

  -O algoritmo def maior foi baseado em
  https://colab.research.google.com/drive/1RzYofml0dFYHMO7JdIJ-M5BUGY5YYK92#scrollTo=1UNcvab7tneT

"""
import math

def SIR (N, Beta, Gama, Tmax) :
    I = []
    R = []
    S = []
    S.append(N - 1)
    I.append(1)
    R.append(0)

    for t in range(Tmax-1):
        S.append(S[t] - Beta*(S[t]*I[t]/N))
        I.append(I[t] + Beta*(S[t]*I[t]/N) - (Gama*I[t]))
        R.append(R[t] + (Gama * I[t]))
    return S,I,R

def maior(L):
  maior = L[0]
  valor = 0
  while valor < len(L):
    if L[valor] > maior:
        maior = L[valor]
    valor += 1
  return maior

def Tetos(valor):
    if int(valor)==valor:
        teto = valor
    elif int(valor)!=valor:
        teto = int(valor)+1
    return teto

def critic_SIR (N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta):
    B = Beta_MIN
    c = 0
    Imax = []

    while B <= Beta_MAX:
        S,I,R = SIR(N,B,Gama,Tmax)
        B += Beta_delta

        #Calcula o qual valor da lista I e maior
        n = len(I)
        vmaximo = 0
        for i in range(1, n) :
            if I[i] > I[vmaximo] :
                vmaximo = i

        Imax.append(I[vmaximo])

    return Imax

def cria_matriz(m, n, valor):
    matriz = []
    linha = [valor]*n
    for i in range(m):
        matriz.append(linha[:])
    return matriz

def gera_grafico_simples(L):
    Y_MIN = 0
    X_MAX = len(L)-1
    X_MIN = 0
    #calcular o valor maximo de L e usar round para conseguir YMAX
    Y_Max = Tetos(maior(L))

    #tamanho da matriz
    m = Y_Max-Y_MIN+1
    n = len(L)
    nulo = 0
    matriz = cria_matriz(m,n,nulo)

    for k in range(len(L)):
        i = round(Y_Max - L[k])
        j = k
        matriz[i][j] = 255

    pgm = open("graf_simples.pgm","w")
    pgm.write("P2\n")
    pgm.write(str(n))
    pgm.write(" ")
    pgm.write(str(m))
    pgm.write("\n")
    pgm.write("255")
    pgm.write("\n")

    for linhaimprime in range(m):
        for colunaimprime in range(n):
            pgm.write(" ")
            pgm.write(str(matriz[linhaimprime][colunaimprime]))
        pgm.write("\n")
    pgm.close()

    return matriz


def gera_grafico_composto(S, I, R):
    Y_MIN = 0
    X_MAX = len(S) - 1
    X_MIN = 0
    # calcular o valor maximo de L e usar round para conseguir YMAX
    Y_Max = Tetos(maior(S))

    # tamanho da matriz
    m = Y_Max - Y_MIN + 1
    n = len(S)
    novaMatriz = cria_matriz(m,3*n,0)

    for k in range(len(S)):
        js = 3*k
        jl = 3*k + 1
        jr = 3*k + 2
        i1 = round(Y_Max - S[k])
        i2 = round(Y_Max - I[k])
        i3 = round(Y_Max - R[k])

        novaMatriz[i1][js] = 255
        novaMatriz[i2][jl] = 255
        novaMatriz[i3][jr] = 255

    ppm = open("graf_composto.ppm", "w")
    ppm.write("\nP3\n")
    ppm.write(str(n))
    ppm.write(" ")
    ppm.write(str(m))
    ppm.write("\n")
    ppm.write("255")
    ppm.write("\n")
    novon = n*3

    for linhaimprime in range(m) :
        for colunaimprime in range(novon) :
            ppm.write(" ")
            ppm.write(str(novaMatriz[linhaimprime][colunaimprime]))
        ppm.write("\n")
    ppm.close()

    return novaMatriz


#texto = file.read().split(",")
def leitura_de_valores(nome_de_arquivo):
    texto = []
    with open(nome_de_arquivo,'r') as arquivo:
        for linha in arquivo:
            texto.append((linha.strip()))
    N = int(texto[0])
    Gama = float(texto[1])
    Tmax = int(texto[2])
    Beta_MIN = float(texto[3])
    Beta_MAX = float(texto[4])
    Beta_delta = float(texto[5])
    return N,Gama,Tmax,Beta_MIN,Beta_MAX,Beta_delta


# Opções
# 1: Calcular 'SIR' e imprimir os vetores S, I e R - leitura de teclado
# 2: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de teclado
# 3: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de arquivo
# # 4: Calcular 'critic_SIR', testar matriz devolvida por 'gera_grafico_simples' - leitura de teclado
# # 5: Calcular 'critic_SIR', testar arquivo PGM no disco por 'gera_grafico_simples' - leitura de teclado
# 6: Calcular 'SIR', testar matriz devolvida por 'gera_grafico_composto' - leitura de teclado
# 7: Calcular 'SIR', testar arquivo PPM no disco por 'gera_grafico_composto' - leitura de teclado

#Não altere as funções abaixo:
def imprimeLista(L) :
    for i in range(len(L)):
      print("%.4f " % L[i], end=""); # usar apenas 4 digitos apos ponto
    print()

def main():
    Opt = int(input("Digite modo do programa: "))
    if (Opt == 1): # saida - SIR; entrada - teclado
        N = int(input("Digite N: "))
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        S,I,R = SIR(N, Beta, Gama, Tmax)
        print("S = ", end="")
        imprimeLista(S)
        print("I = ", end="")
        imprimeLista(I)
        print("R = ", end="")
        imprimeLista(R)
    elif (Opt == 2): # saida - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: "))
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 3): # saida - critic_SIR; entrada - arquivo
        Dados = input("Digite nome do arquivo: ");
        N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leitura_de_valores(Dados)
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        imprimeLista(c_SIR)
    elif (Opt == 4): # grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: "))
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        print(M_grafico)
    elif (Opt == 5): # PGM - grafico simples - critic_SIR; entrada - teclado
        N = int(input("Digite N: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        Beta_MIN = float(input("Digite Beta_MIN: "))
        Beta_MAX = float(input("Digite Beta_MAX: "))
        Beta_delta = float(input("Digite Beta_delta: "))
        c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
        M_grafico = gera_grafico_simples(c_SIR)
        g = open("graf_simples.pgm", "r")
        print(g.read())
        g.close()
    elif (Opt == 6): # grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: "))
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        print(M_grafico)
    elif (Opt == 7): # PPM - grafico composto - SIR; entrada - teclado
        N = int(input("Digite N: "))
        Beta = float(input("Digite Beta: "))
        Gama = float(input("Digite Gama: "))
        Tmax = int(input("Digite Tmax: "))
        S,I,R = SIR(N, Beta, Gama, Tmax)
        M_grafico = gera_grafico_composto(S, I, R)
        g = open("graf_composto.ppm", "r")
        print(g.read())
        g.close()

main()
