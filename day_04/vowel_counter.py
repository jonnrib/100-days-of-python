palavra = input("Palavra: ").lower()
vogais = "aeiou"
contador = 0

print()

for letras in palavra:
  if letras in vogais:
    contador += 1

print(f"\"{palavra}\" tem {contador} vogais.")
