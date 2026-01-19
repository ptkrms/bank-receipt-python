# Classe base que representa uma conta genérica do cliente
# Serve como base para contas comuns e contas remuneradas

class ContaCliente:
    def __init__(self, numero, iof, ir, valor_investido, taxa_rendimento):
        # Número identificador da conta
        self.numero = numero

        # Percentual de IOF aplicado sobre o rendimento
        self.iof = iof

        # Percentual de Imposto de Renda aplicado sobre o rendimento
        self.ir = ir

        # Valor atualmente investido na conta
        self.valor_investido = valor_investido

        # Taxa de rendimento aplicada ao valor investido
        self.taxa_rendimento = taxa_rendimento

    # Método responsável por calcular o rendimento da conta
    # Aplica a taxa de rendimento e desconta IOF e IR
    def calcular_rendimento(self):
        # Calcula o valor bruto do rendimento
        rendimento_bruto = self.valor_investido * self.taxa_rendimento

        # Calcula os descontos
        desconto_iof = rendimento_bruto * self.iof
        desconto_ir = rendimento_bruto * self.ir

        # Atualiza o valor investido com o rendimento líquido
        self.valor_investido += rendimento_bruto - desconto_iof - desconto_ir

    # Exibe o saldo atual da conta
    def extrato(self):
        print(
            f"Saldo atual da conta {self.numero}: "
            f"R$ {self.valor_investido:,.2f}"
        )
