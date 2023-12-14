from datetime import date

class Pessoa:
    
    

    def __init__(self, nome, nascimento, cpf, rg, endereço, estado_civil):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.rg = rg 
        self.endereço = endereço
        self.estado_civil = estado_civil
        self.idade = self.calcular_idade(nascimento)
    
    
    def calcular_idade(self, nascimento):
        nascimento_formatado = self.nascimento.split('/')

        dia_nascimento = int(nascimento_formatado[0])
        mes_nascimento = int(nascimento_formatado[1])
        ano_nascimento = int(nascimento_formatado[2])
        
        return date.today().year - ano_nascimento 
           
        
    