b = open('F:/Andrew/Удалить/new 2.txt', 'r', encoding='utf')

lines = [line.strip() for line in b]
for v in lines:
    print(v)
