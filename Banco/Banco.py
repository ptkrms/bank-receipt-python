# Classe Banco
# Responsável por gerenciar um conjunto de contas
# e aplicar o cálculo de rendimento mensal utilizando polimorfismo

class Banco:
    def __init__(self, codigo, nome):
        # Código identificador do banco
        self.codigo = codigo

        # Nome do banco
        self.nome = nome

        # Lista de contas associadas ao banco
        self.contas = []

    # Adiciona uma conta ao banco
    def adicionar_conta(self, conta_cliente):
        self.contas.append(conta_cliente)

    # Aplica o cálculo de rendimento mensal em todas as contas
    # Este método utiliza POLIMORFISMO:
    # cada conta executa sua própria implementação de calcular_rendimento
    def calcular_rendimento_mensal(self):
        for conta in self.contas:
            conta.calcular_rendimento()

    # Imprime o saldo (extrato) de todas as contas do banco
    def imprimir_saldos(self):
        for conta in self.contas:
            conta.extrato()
