ano = 365
mes = 30

while True:
  dia_atual = int(input("Digite o dia atual (1 a 30): "))
  if 1 <= dia_atual <= 30:
    break
  print("Valor incorreto! \n")

while True:
  mes_atual = int(input("Digite o mês atual (1 a 12): "))
  if 1 <= mes_atual <= 12:
    break
  print("Valor incorreto! \n")

while True:
  ano_atual = int(input("Digite o ano atual: "))
  if ano_atual > 0:
    break
  print("Valor incorreto! \n")

print()

while True:
  dia_ani = int(input("Digite o dia em que você nasceu (1 a 30): "))
  if 1 <= dia_ani <= 30:
    break
  print("Valor incorreto! \n")

while True:
  mes_ani = int(input("Digite o mês em que você nasceu (1 a 12): "))
  if 1 <= mes_ani <= 12:
    break
  print("Valor incorreto! \n")

while True:
  ano_ani = int(input("Digite o ano em que você nasceu: "))
  if ano_ani > 0:
    break
  print("Valor incorreto! \n")

print()

total_atual = (ano_atual * ano) + (mes_atual * mes) + dia_atual
total_ani = (ano_ani * ano) + (mes_ani * mes) + dia_ani
print(f"São {total_atual - total_ani} dias desde o seu nascimento!")
