class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

class Pessoa:
    def __init__(self, nome, idade, carro):
        self.nome = nome
        self.idade = idade
        self.carro = carro


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25, meucarro)


print('Nome: ', eu.nome)  
print('Idade: ', eu.idade)
print('Marca do carro: ', eu.carro.marca)  
print('Modelo do carro: ', eu.carro.modelo)
print('Placa do carro: ', eu.carro.placa)
print('Ano do carro: ', eu.carro.ano)

        
        
