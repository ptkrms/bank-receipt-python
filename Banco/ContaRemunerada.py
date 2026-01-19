from ContaCliente import ContaCliente

#classe com herança de conta cliente

class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)
        #redefine o metodo calculo_rendimento para aplicar a taxa de rendimento sem aplicar nenhum imposto

    def calculoRendimento(self):
        self.valor_investido += self.valor_investido * self.taxa_rendimento