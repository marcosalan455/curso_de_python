
#exercício prático

'''
Criar um algoritmo que:
solicite o nome, idade, telefone e endereço completo.
Passar as informações das váveis com  print formatado respeitando
cada resultado em uma linha.
o print para ficar melhor visível deverá após o barra invertida n precionar enter.
'''

nome = str(input("digite seu nome: "))
idade = int(input("digite sua idade: "))
telefone = str(input("digite seu telefone: "))
rua = str(input("digite o nome de sua rua: "))
bairro = str(input("digite seu bairro: "))
numero = int(input("digite o número: "))
cep = str(input("digite o cep de sua rua: "))

print(f"olá: {nome}\n"
      f" Sua idade é: {idade} anos\n"
      f" seu telefone é: {telefone}\n"
      f" você mora na rua {rua}\n"
      f"de número {numero}\n"
      f"no bairro {bairro}\n"
      f"com o CEP {cep}"
      )

