# for variavel_de_controle in range(0,20):
#     print(variavel_de_controle)

# lista = [1, 5, 15]

# for e in lista:
#     print(e)

# lista = ["joao", "francisco", "chico"]

# for e in lista:
#     print(e)

# lista = [7, 9, 10, 12]

# p = int(input("digite um numero a pesquisar: "))
# for e in lista:
#     if e == p:
#         print("elemento encontrado")
#         break
#     else:
#         print("elemento nao encontrado")

# FUNÇÃO RANGE

# for imprime_9 in range(1, 10, 2):
#     print(imprime_9)

# FUNÇÃO END NA LISTA

# for t in range(3, 33, 3):
#     print(t, end=" ")
# print(t)

# f = list(range(100, 1100, 50))
# print(f)

# LISTA DE NUMEROS PARES ATE 50

# from time import sleep

# for par in range(2,51,2):
#     print(par, end=", ")
#     sleep(0.5)
# print('numeros pares ate 50.....')

# for i in range(0, 10):
#     print(i+1)
# print('fim')

# for i in range(10, -1, -1):
#     print(i)
# print('fim')

# (RANGE) INTERAÇÃO COM O USUARIO

# numero = int(input('digite um numero'))
# for i in range(0, numero+1):
#     print(i)
#     print('fim')

# inicio = int(input('inicio: '))
# fim = int(input('fim: '))
# passo = int(input('passo: '))

# for i in range(inicio, fim+1, passo):
#     print(i)
# print('fim')


# soma = 0  
# fim = int(input('digite quantos numeros deseja somar: '))
# for i in range(0,fim):
#     numero = int(input('digite um valor: '))
#     soma += numero
# media = soma/fim
# print(f'a soma dos numeros foi: {soma}, e a media foi {media: .2f}

# CONTAGEM REGRESSIVA

from time import sleep
import random
for i in range(1, 11, 1):
    print("Hackeando a NASA", i*10, "%")
    sleep(random.randint(1, 5))
print('Hackeado com sucesso!')