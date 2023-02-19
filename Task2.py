
n = int(input("N = "))
a = []
for i in range(n):
    a.append(int(input(f"A[{i}] = ")))

max = 0
for x in range(n):
    sum = a[(x - 1) % n] + a[x % n] + a[(x + 1) % n]
    if sum > max:
        max = sum

print(f"max = {max}")

