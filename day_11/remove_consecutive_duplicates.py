arrays = map(int, input("Digite os números (separados por espaço): ").split())
numbers = list(arrays)

current_number = numbers[0]
new_list = [current_number]

for number in numbers[1:]:
  if number != current_number:
    new_list.append(number)
    current_number = number

print(new_list)
