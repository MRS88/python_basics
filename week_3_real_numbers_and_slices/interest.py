p, x, y, k = int(input()), int(input()), int(input()), int(input())
total = (x * 100 + y) * (100 + p) / 100
while k != 1:
    total += total * (p / 100)
    k -= 1
print(int(total // 100), int(total % 100))
