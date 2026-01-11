numbers = map(int, input("Digite os números (separados por espaço): ").split())
numbers_list = list(numbers)

current_max = numbers_list[0]

for number in numbers_list[1:]:
  if number > current_max:
    current_max = number

print(f"O maior número da lista é {current_max}!")
