# como definir uma classe

class Carro:
    cor = "vermelho"
    marca = "Honda" 
    modelo =  "H-rv"

    def ligar_motor(self):
        print("vrum vrum")
        
carro = Carro()
print(carro.marca)
print(carro.cor)

carro.ligar_motor()

print("\n" + "#"*10, "NOVO CARRO" , "#"*10 + "\n")

novo_carro = Carro()
print(novo_carro.marca)

novo_carro.cor ="branco"
print(novo_carro.cor)

carro.ligar_motor()
