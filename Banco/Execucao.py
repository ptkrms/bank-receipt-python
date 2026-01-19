from Banco import Banco
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada
from ContaCliente import ContaCliente


banco1 = Banco(999,"teste")
conta_cliente1 = ContaCliente(1,0.01,0.1,1000,0.05)
conta_comum1 = ContaComum(2,0.01,0.1,2000,0.05)
conta_remunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adiciona_conta(conta_cliente1) #(4)
banco1.adiciona_conta(conta_comum1) #(5)
banco1.adiciona_conta(conta_remunerada1) #(6)
banco1.calcular_rendimento_mensal()  #(7)
banco1.imprime_saldo_contas()  #(8)