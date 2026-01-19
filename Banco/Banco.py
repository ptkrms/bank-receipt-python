#classe que gerencia todas as contas e calcula o rendimento mensal

class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    #metodos para adicionar contas, calcular o rendimento mensal, imprimir o saldo das contas

    def adiciona_conta(self, conta_cliente):
        self.contas.append(conta_cliente)

    #este metodo é polimorfico e tem uma implementação diferente em casa classe
    def calcular_rendimento_mensal(self):
        for c in self.contas:
            c.calculoRendimento()

    def imprime_saldo_contas(self):
        for c in self.contas:
            c.extrato()

