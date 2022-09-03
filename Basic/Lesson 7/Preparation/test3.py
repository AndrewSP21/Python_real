# a = [[31, 22], [37, 43], [51, 86]]
# a += [11, 12]
# print(f'a= {a}')
# b = [[31, 22], [37, 43], [51, 86]]
# b.append([11, 12])
# print(f'b= {b}')
#

# data = ''.join(['*' for i in range(0, 20)]) + '\\n'
# print(data)

a = '********************'
print(len(a))
# a.index(2) ='Y'
print(a)
b=''
count = 4
for i in a:
    b += i if i % count == 0 else i + '\\n'

print(b)