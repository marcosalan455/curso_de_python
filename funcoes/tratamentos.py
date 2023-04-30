
def leiaInt(msg):
    while True:
        try:
            n =int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro válido!")
            continue
        except(KeyboardInterrupt):
            print("Programa enterrompido pelo usuário, FIM...")
            break
        else:
            return n

