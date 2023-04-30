#algoritmo com opções de menu

print('''
[1] - soma,
[2] - subtração,
[3] - multiplicação,
[4] - divisão,
[5] - sair
''')
opc = int(input("Escolha uma opção: "))


if opc == 1:
    n1 = int(input("digite um número: "))
    n2 = int(input("Digite outro número: "))
    soma = n1 + n2
    print(f"a soma entre {n1} e {n2} é igual a {soma}")
elif opc == 2:
    n1 = int(input("digite um número: "))
    n2 = int(input("Digite outro número: "))
    subtracao = n1 - n2
    print(f"a subtração entre {n1} e {n2} é igual a {subtracao}")
elif opc == 3:
    n1 = int(input("digite um número: "))
    n2 = int(input("Digite outro número: "))
    multiplicacao = n1 * n2
    print(f"a multiplicação entre {n1} e {n2} é igual a {multiplicacao}")
elif opc == 4:
    n1 = int(input("digite um número: "))
    n2 = int(input("Digite outro número: "))
    divisao = n1 / n2
    print(f"a divisão entre {n1} e {n2} é igual a {divisao}")
elif opc == 5:
    print("saindo do sistema, até logo!")
else:
    print("ERRO: por favor digite um valor válido.")
print("fim")

