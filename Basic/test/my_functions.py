a = [1, 5, 1, 5, 1, 6]
m = [j for i, j in zip(a, a[1:]) if j > i]
v = list(zip(a, a[1:]))
print(v)
print(a[1:])
print(m)