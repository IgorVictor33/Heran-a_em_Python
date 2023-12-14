#lista 
# P[0], P[1] -> P[5]

# lista = [1,2,3]
# print(lista)

# lista[0] = 0
# print(lista)

# notas =[6, 7, 5, 8, 9,]
# soma = 0
# x = 0
# while x < 5:
#     soma += notas[x]
#     x += 1
# print(f"media: {soma/ x: .2f}")

notas = [0,0,0,0,0]
soma = 0 
x = 0 
while x < 5:
    notas[x] = float(input(f'digite a {x+1}ª nota: '))
    soma += notas[x]
    x += 1
x = 0
print(" ")
print('suas notas bimestre a bimestre')
while x < 5:
    print(f'{x+1}ª nota: {notas[x]: .2f}')
    x += 1
print(" ")
print(f'media: {soma /x : .2f}')