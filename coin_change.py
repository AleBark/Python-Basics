# -*- coding: utf-8 -*-

"""
Ale Bark Bruneri
"""

def main(arr_moedas_disponiveis):
    print("________________ \n")

    if arr_moedas_disponiveis:

        valor_conta = input("Valor da conta:")
        valor_pago = input("Valor pago:")

        condicoes_de_execucao = [
            validar_entrada_float(valor_conta),
            validar_entrada_float(valor_pago),
        ]

        if all(condicoes_de_execucao):
            valor_pago = float(valor_pago)
            valor_conta = float(valor_conta)

            if valor_pago >= valor_conta:
                if valor_pago - valor_conta == 0:
                    print("Valor ok, não há necessidade de troco!")
                    return False
                return calcular_troco(round(valor_pago - valor_conta, 2), arr_moedas_existentes, arr_moedas_disponiveis)

        print("Valores inválidos, reiniciando!")
        return False


def validar_entrada_moedas(arr_moedas_existentes):
    arr_moedas_disponiveis = []
    for moeda in arr_moedas_existentes:
        print("Qtde de moedas de " + str(moeda) + "", "real" if moeda == 1 else "centavos:")
        moeda_da_vez = input()

        if not validar_entrada_int(moeda_da_vez):
            print("Valor inválido, reiniciando \n")
            return False

        arr_moedas_disponiveis.append(int(moeda_da_vez))
    return arr_moedas_disponiveis


def validar_entrada_int(input):
    try:
        valor = int(input)
        return valor >= 0
    except ValueError:
        return False


def validar_entrada_float(input):
    try:
        valor = float(input)
        return valor > 0
    except ValueError:
        return False


def calcular_troco(troco, arr_moedas_existentes, arr_moedas_disponiveis):
    print("Troco:", troco, '\n')
    arr_moedas_troco = [0, 0, 0, 0, 0]

    for x in range(len(arr_moedas_existentes)):
        quantidade_moeda = 0
        while troco >= arr_moedas_existentes[x]:
            if arr_moedas_disponiveis[x] >= 1:
                troco = round(troco - arr_moedas_existentes[x], 2)
                quantidade_moeda += 1
                arr_moedas_troco[x] = quantidade_moeda
                arr_moedas_disponiveis[x] = arr_moedas_disponiveis[x] - 1
            else:
                break

    if troco != 0:
        print("Quantidade de moedas em caixa insuficiente, faltaram", troco, "reais.. reiniciando")
        return False

    print("Troco fornecido ao cliente [1 real, 0.50 centavos, 0.25 centavos, 0.10 centavos, 0.05 centavos] :",
          arr_moedas_troco)
    print("Troco atual na máquina [1 real, 0.50 centavos, 0.25 centavos, 0.10 centavos, 0.05 centavos] :",
          arr_moedas_disponiveis)
    return True


if __name__ == '__main__':
    arr_moedas_existentes = [1, 0.5, 0.25, 0.10, 0.05]
    arr_moedas_disponiveis = validar_entrada_moedas(arr_moedas_existentes)

    while True:
        main(arr_moedas_disponiveis)
