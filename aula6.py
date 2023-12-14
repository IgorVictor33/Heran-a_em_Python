# estrutura de repetição 
# while <condição>:
# bloco a ser executado

x = 1
while x <= 100: 
    print(x)
    x += 1


# Exercicio 5.1 modifique o programa para exibir os numeros de 1 a 100

'''
contagem = 1
while contagem <= 100:
    print(contagem)
    contagem += 1

# exercicio 5.2 modifique o programa para receber os numeros de 50 a 100
'''
'''
contagem = 50
while contagem <= 100:
    print(contagem)
    contagem += 1
'''
'''
# exercicio 5.3 faça uma contagem regressiva
regresso = 10
while regresso >= 0:
    print(regresso)
    regresso -= 1
print('fogo!')
'''
# estrutura de repetição 
'''
fim = int(input('digite o fim da repetição: '))
x = 1
while x <= fim:
    print(x)
    x = x + 1
'''
'''
fim = int(input('digite o fim da repetição: '))
x = 1000
while x <= fim:
    print(x)
    x = x + 5000
'''
'''
# estrutura de repetição par
fim = int(input('digite o ultimo numero a ser impresso: '))

x = 0 
while x <= fim:
    if x % 2 == 0:
        print(x)
    x +=  1
'''
'''
# estrutura de repetição impar
fim = int(input('digite o ultimo numero a ser impresso: '))

x = 1 
while x <= fim:
    if x % 3 == 0:
        print(x)
    x += 1
'''
'''
# impressão de numeros pares e impares
fim = int(input('digite o ultimo numero a ser impresso: '))

x = 0
while x <= fim:
    if x % 2 == 0:
        print(f'o numero {x} é par')
    else:
        print(f'o numero {x} é impar') 
    x += 1
'''
'''
# operaçoes de tabuada

numero = int(input(f'Tabuada de: '))
contador = 1 
print(f'*** tabuada de {numero}***')
while contador <= 10:
    print(numero + contador)
    contador += 2
'''
# exercicio 5.6
numero = int(input(f'tabuada de: '))
contador = 1 

while contador <= 10:
    print (f'{numero} X {contador} = {numero * contador}')
    contador += 1

# exercicio 5.7







        
   



