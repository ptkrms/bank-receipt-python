from ContaCliente import ContaCliente

#classe com heranca de contacliente

class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    #redefine o metodo calculo_rendimento para aplicar a taxa de rendimento e descontar apenas o IOF
    def calculoRendimento(self):
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF