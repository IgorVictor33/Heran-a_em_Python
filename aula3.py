# como criar uma string vazia#
tipo_de_pao = 'assado'
string = f'joão e maria comem pão {tipo_de_pao}'
print(string)
print(len(string))
string_vazia = ''
print(len(string_vazia))

# como definir o indice de uma string#
a = 'abcde'
print(a[1])
print(a[3])
#como fazer uma concatenação (junção)
b = "ABC" + "DE - "
print(b)
# como multiplicar as posições
c = "-x-" * 9
print(c)
# concatenações + multiplicações 
f = c + " 4$ = " + b * 4
print(f)
# # oque não fazer...
# g = "Igor"
# h = 10
# print(g + h) 

#composição

anos = 10 
print('joão tem %d anos' % anos )

# %d --> inteiros
# %s ---> strings
# f ------> numeros flutuantes 

#""%03d"

idade = 22
print('%d' % idade)
print('%3d' % idade)
print('%03d' % idade)

reais = 250.5000
print(f'R${reais: .2f}')

# fatiamento de string
i = "ABCDEFGHI"

print(i[5:7]) #posição inicial: ate essa posição
print(i[5:7][::-1]) #reversão (i[6:4:-1])

#reversão

j = "DVD da XUXA ao contrário"
print(j[::-1])

divida = 0
compra = 100
divida = compra + divida 
compra = 200
divida = compra + divida
compra = 300
divida = compra + divida 

print(divida)

# entrada de dados
'''
x = input("digite aqui: ")
print(f'o texto digitado foi {x}')
print(x)
'''
'''
nome = input("digite aqui o seu nome: ")
print(nome)
print(f'voce digitou o seu nome {nome}')
'''
'''
numero = int(input('digite um numero'))
print(type(numero))

reais = float(input('digite um valor para reais: '))
print(f'voce tem apenas R${reais: .2f}')
'''
'''
dias = int(input('Quantos dias: '))
horas = int(input('Quantos horas: '))
minutos = int(input('Quantos minutos: '))
segundos = int(input('Quantos segundos: '))

dia = (60*60)*24
hora = 60*60
minuto = 60
segundos_totais = (dia * dias) + (hora * horas) + (minuto * minutos) + segundos 

print(segundos_totais)
'''

#condicional IF
# if <condição>:
#     bloco verdadeiro
# exemplo
'''
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))

if a > b:
    print('O primeiro valor é o maior')

if b > a: 
    print('O segundo valor é o maior')

if a == b:
    print(' Os valores são iguais!')

print('fim do programa.')



idade = int(input('qual a idade do seu carro: '))
if idade <=3:
    print('seu carro é novo!')

if idade >3:
    print('seu carro é velho!')

'''

#exercicio 4.2
'''
velocidade = int(input('qual foi a sua velocidade: '))

if velocidade >80:
    multa = velocidade*5 
    print(f'voce foi multado em R$: {multa}')

if velocidade <=80: 
    print(f'voce deu sorte!')

'''

# EXERCICIO 4.3

a = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
c = int(input('digite o terceiro numero: '))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b 
if c < b and c < a:
    menor = c

print(f'o menor numero foi digitado {menor}')
print(f'o maior numero foi digitado {maior}')    
