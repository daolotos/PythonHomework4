
n = int(input("N = "))
m = int(input("M = "))
a = set()
for i in range(n):
    a.add(int(input(f"A[{i}] = ")))
b = set()
for i in range(n):
    b.add(int(input(f"B[{i}] = ")))

print(sorted(a.intersection(b)))
