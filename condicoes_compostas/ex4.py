
nome = str(input("digite seu nome: "))
valor = float(input("Qual o valor que você possui: "))

if valor <= 50:
    print(f"olá {nome} você tem: R${valor:.2f} você está pobre.")
elif valor <= 100:
    print(f"olá {nome} Você tem R${valor:.2f} agora você já está me convencendo.")
elif valor <= 250:
    print(f"Olá {nome} você tem R${valor:.2f} Gostei de ver!")
else:
    print(f"Olá {nome} Você tem R${valor:.2f} muito bom, você é uma pessoa bem sucedida!")


