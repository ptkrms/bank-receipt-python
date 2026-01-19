from ContaCliente import ContaCliente

# Classe ContaRemunerada
# Representa uma conta que possui rendimento
# sem a aplicação de IOF ou IR
class ContaRemunerada(ContaCliente):

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
    # Aplica apenas a taxa de rendimento, sem desconto de impostos
    def calcular_rendimento(self):
        rendimento = self.valor_investido * self.taxa_rendimento
        self.valor_investido += rendimento
