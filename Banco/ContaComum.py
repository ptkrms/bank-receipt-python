from ContaCliente import ContaCliente

# Classe ContaComum
# Representa uma conta que possui rendimento,
# mas sofre desconto apenas de IOF (não há IR)
class ContaComum(ContaCliente):

    def __init__(self, numero, iof, ir, valor_investido, taxa_rendimento):
        # Inicializa os atributos herdados da classe ContaCliente
        super().__init__(
            numero=numero,
            iof=iof,
            ir=ir,
            valor_investido=valor_investido,
            taxa_rendimento=taxa_rendimento
        )

    # Sobrescrita do método calcular_rendimento (polimorfismo)
    # Aplica a taxa de rendimento e desconta apenas o IOF
    def calcular_rendimento(self):
        # Calcula o rendimento bruto
        rendimento_bruto = self.valor_investido * self.taxa_rendimento

        # Calcula o desconto de IOF
        desconto_iof = rendimento_bruto * self.iof

        # Atualiza o valor investido com o rendimento líquido
        self.valor_investido += rendimento_bruto - desconto_iof
