records = []

for i in range(int(input("Quantidade: "))):
    name = input("Nome: ")
    grade = float(input("Nota: "))

    scores = [name, grade]
    records.append(scores)

print(records)
