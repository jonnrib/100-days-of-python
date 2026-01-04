total_eleitores = int(input("Número de eleitores: "))
print()

while True:
  votos_validos = int(input("Número de votos válidos: "))
  votos_brancos = int(input("Número de votos brancos: "))
  print()


  if votos_validos < 0 or votos_brancos < 0:
    print("O número não pode ser negativo!")
    continue

  if votos_validos + votos_brancos > total_eleitores:
    print("O número ultrapassa o total! \n")
    continue

  votos_nulos = total_eleitores - (votos_validos + votos_brancos)

  porcent_brancos = (votos_brancos / total_eleitores) * 100
  porcent_nulos = (votos_nulos / total_eleitores) * 100
  porcent_validos = (votos_validos / total_eleitores) * 100

  print(
      "Distribuição dos votos: \n"
      f"- Votos válidos: {porcent_validos:.2f}%\n"
      f"- Votos brancos: {porcent_brancos:.2f}%\n"
      f"- Votos nulos: {porcent_nulos:.2f}%"
      )
  break
