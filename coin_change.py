# -*- coding: utf-8 -*-

def main():
    arr_moedas_existentes = [1, 50, 25, 10, 5]
    arr_moedas_disponiveis = validar_moedas_disponiveis(arr_moedas_existentes)

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
                return calcular_troco(valor_pago - valor_conta, arr_moedas_existentes, arr_moedas_disponiveis)

        print("Valores inválidos, reiniciando!")
        return False


def calcular_troco(troco, arr_moedas_existentes, arr_moedas_disponiveis):
    print("Troco fornecido:", troco, '\n')

    if troco != 0:
        for x in range(len(arr_moedas_existentes)):
            x = x
    return True


def validar_moedas_disponiveis(arr_moedas_existentes):
    arr_moedas_disponiveis = []
    for moeda in arr_moedas_existentes:
        print("Qtde de moedas de " + str(moeda) + "", "real" if moeda == 1 else "centavos:")
        moeda_da_vez = input()

        if not validar_entrada_int(moeda_da_vez):
            print("Valor inválido, reiniciando \n")
            return False

        arr_moedas_disponiveis.append(moeda_da_vez)
    return arr_moedas_disponiveis


def validar_entrada_float(input):
    try:
        valor = float(input)
        return valor > 0
    except ValueError:
        return False


def validar_entrada_int(input):
    try:
        valor = int(input)
        return valor > 0
    except ValueError:
        return False


if __name__ == '__main__':
    while True:
        main()
