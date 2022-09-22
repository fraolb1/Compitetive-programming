m, n = map(int, input.split())
total = m * n
count = 0
while total >= 0:
    if total < 2:
        print(count)
    count += 1
    total -= 2