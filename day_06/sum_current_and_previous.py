total = 0
previous = 0

for current in range(10):
    total = current + previous
    print(f"Current {current} + Previous {previous} = {total}")
    previous = current
