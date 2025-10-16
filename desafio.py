from calculo import dobro, triplo, quadrado

def calculardobro():
  numero = float(input("Digite um numero: "))
  dobronum = dobro(numero)
  print(f"O dobro e {numero} é {dobronum}")
def calculartriplo():
  numero = float(input("Digite um numero: "))
  triplonum = triplo(numero)
  print(f"O triplo de {numero} é {triplonum}")
def calcularquadrado():
  numero = float(input("Digite um numero: "))
  quadradonum = quadrado(numero)
  print(f"O quadrado de {numero} é {quadradonum}")
  
while True:
  print("Escolha uma opção:")
  print("1 - Calcular o dobro")
  print("2 - Calcular o triplo")
  print("3 - Calcular o quadrado")
  print("4 - Sair")
  opcao = int(input("Digite a opção desejada: "))
  if opcao == 1:
    calculardobro()
  elif opcao == 2:
    calculartriplo()
  elif opcao == 3:
    calcularquadrado()
  elif opcao == 4:
    print("Finalizando Serviço...")
    break
  else:
    print("Opção inválida")
