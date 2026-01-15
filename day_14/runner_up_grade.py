records = []

for _ in range(int(input("Quantidade: "))):
    name = input("Nome: ")
    grade = float(input("Nota: "))
    records.append([name, grade])

notes = []
for name, grade in records:
    notes.append(grade)

highest = notes[0]
for value in notes[1:]:
    if value > highest:
        highest = value

runner_up = None
for value in notes:
    if value != highest:
        if runner_up is None or value > runner_up:
            runner_up = value

if runner_up is None:
    print("No runner-up (all values are equal).")
else:
    print(runner_up)
