# -*- coding: utf-8 -*-

def main():

    arr_moedas_disponiveis = []
    arr_moedas_disponiveis[0] = input("Qtde de moedas de um real: ")
    arr_moedas_disponiveis[1] = input("Qtde de modedas de cinquenta centavos: ")
    arr_moedas_disponiveis[2] = input("Qtde de moedas de vinte e cinco centavos: ")
    arr_moedas_disponiveis[3] = input("Qtde de moedas de dez centavos: ")
    arr_moedas_disponiveis[4] = input("Qtde de moedas de cinco centavos: ")

    if validar_moedas_disponiveis(arr_moedas_disponiveis):

        valor_conta = input("Valor da conta:")
        valor_pago = input("Valor pago:")

        condicoes_de_execucao = [
            valor_conta,
            valor_pago,
            validar_entrada_float(valor_conta),
            validar_entrada_float(valor_pago),
        ]

        if all(condicoes_de_execucao):

            valor_pago = float(valor_pago)
            valor_conta = float(valor_conta)

            if valor_pago >= valor_conta:
                calcular_troco(valor_pago - valor_conta, arr_moedas_disponiveis)
            else:
                print("Valor pago insuficiente \n")
                return False
        print("Condições de execução não foram atendidas, abortando!")
        return True


def calcular_troco(troco, arr_moedas_disponiveis):

    trocos_possieis = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.5, 0.1]
    changes_quantity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    print("Troco fornecido:", troco, '\n')
    if change != 0:
        for x in range(len(posible_changes)):
            cont = 0
            while change >= posible_changes[x]:
                change = change - posible_changes[x]
                cont += 1
                changes_quantity[x] = cont
    print(posible_changes, '-', changes_quantity)


def validar_moedas_disponiveis(arr_moedas_disponiveis):
    for moeda in arr_moedas_disponiveis:
        return validar_entrada_float(moeda)
    return True


def validar_entrada_float(input):
    try:
        valor = float(input)
        return valor > 0
    except ValueError:
        print("Entrada inválida")
        return False


if __name__ == '__main__':
    while True:
        main()
