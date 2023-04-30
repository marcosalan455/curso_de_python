
idade = int(input("Digite sua idade: "))

if idade <= 18:
    print(f"Sua idade é: {idade} anos, \nvocê ainda não precisa se alistar.")
elif idade <= 21:
    print(f"Sua idade é: {idade} anos\nVocê já pode se alistar.")
else:
    print(f"Sua idade é: {idade} anos\nSeu praso de alistamento já passou.")

