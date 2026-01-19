from Banco import Banco
from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada


banco1 = Banco(999, "teste")

conta_cliente1 = ContaCliente(1, 0.01, 0.1, 1000, 0.05)
conta_comum1 = ContaComum(2, 0.01, 0.1, 2000, 0.05)
conta_remunerada1 = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

banco1.adicionar_conta(conta_cliente1)
banco1.adicionar_conta(conta_comum1)
banco1.adicionar_conta(conta_remunerada1)

banco1.calcular_rendimento_mensal()
banco1.imprimir_saldos()
