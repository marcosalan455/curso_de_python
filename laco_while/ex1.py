
n1 = int(input("digite um número: "))
n2 = int(input("Digite outro número: "))

opc = 0

while opc != 7:
    print('''
    [1] - soma,
    [2] - subtração,
    [3] - multiplicação,
    [4] - divisão,
    [5] - maior,
    [6] - novos números,
    [7] - sair do programa
    ''')
    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        soma = n1 + n2
        print(f"a soma entre {n1} + {n2} é {soma}")
    elif opc == 2:
        subtracao = n1 - n2
        print(f"a subtração entre {n1} + {n2} é {subtracao}")
    elif opc == 3:
        multiplicacao = n1 * n2
        print(f"a multiplicação entre {n1} e {n2} é {multiplicacao}")
    elif opc == 4:
        divisao = n1 / n2
        print(f"a divisão entre {n1} e {n2} é {divisao:.2f}")
    elif opc == 5:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"entre {n1} e {n2} o maior é: {maior}")
    elif opc == 6:
        print("Informe os números novamente!")
        n1 = int(input("digite um número: "))
        n2 = int(input("Digite outro número: "))
    elif opc == 7:
        print("finalizando...")
    else:
        print("opção inválida, tente novamente...")
print("fim do programa, volte sempre!")