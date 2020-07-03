# -*- coding: utf-8 -*-

def main():
    print("________________ \n")
    arr_moedas_existentes = [1, 0.5, 0.25, 0.10, 0.05]
    arr_moedas_disponiveis = validar_entrada_moedas(arr_moedas_existentes)

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
                return calcular_troco(valor_pago - valor_conta, arr_moedas_existentes, arr_moedas_disponiveis)

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

    # troco = 10.21
    # existente  [1, 0.5, 0.25, 0.10, 0.5]
    # disponivel [3,  0,   0,    0,    1 ]

    for x in range(len(arr_moedas_existentes)):
        quantidade_moeda = 0
        while troco >= arr_moedas_existentes[x]:
            if arr_moedas_disponiveis[x] >= 1:
                troco = troco - arr_moedas_existentes[x]
                quantidade_moeda += 1
                arr_moedas_troco[x] = quantidade_moeda
                arr_moedas_disponiveis[x] = arr_moedas_disponiveis[x] - 1

    if troco != 0:
        print("Quantidade de moedas em caixa insuficiente, reiniciando")
        return False

    print(arr_moedas_troco)
    return True


if __name__ == '__main__':
    while True:
        main()
