class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco * produto.quantidade
        return soma

cafe = Produto('Café Solúvel', 1, 1)
arroz = Produto('Arroz Integral', 1, 3)
feijao = Produto('Feijão Preto', 1, 1)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())

        