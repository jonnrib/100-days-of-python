arr = map(int, input().split())
numbers_list = list(arr)

new_list = []

for number in numbers_list:
  if number not in new_list:
    new_list.append(number)

highest = new_list[0]
for number in new_list[1:]:
  if number > highest:
    highest = number

runner_up = None
for number in new_list:
  if number != highest:
    if runner_up is None or number > runner_up:
      runner_up = number

print(runner_up)
