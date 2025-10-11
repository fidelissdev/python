import fidelis

def dobro(numero):
    return int(numero) * 2

x = input("Digite o número para ser duplicado: ")

dobro = fidelis.dobro(x)

print(f"O dobro de {x} é {dobro}")


def triplo(numero):
    return int(numero) * 3

x = input("Digite o número para ser triplicado: ")

triplo = fidelis.triplo(x)

print(f"O triplo de {x} é {triplo}")