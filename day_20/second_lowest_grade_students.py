records = []

for _ in range(int(input("Quantidade: "))):
    names = input("Nome: ")
    grades = float(input("Nota: "))
    records.append([names, grades])

notes = []
for name, grade in records:
    if grade not in notes:
        notes.append(grade)

lowest = notes[0]
for grade in notes[1:]:
    if grade < lowest:
        lowest = grade

second_lowest = None
for grade in notes:
    if grade != lowest:
        if second_lowest is None or grade < second_lowest:
            second_lowest = grade

records.sort()
for name, grade in records:
    if grade == second_lowest:
        print(name)
