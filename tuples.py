x = ('Apple', 'Banana', 'Cherry', 'Strawberry', 'Pineapple')

print(x)
print(x[1])

x = list(x)
print(x)
print(x[1])

x.append('Apple')
print(x)
print(x[1])

x[1] = 'Kiwi'
x = tuple(x)
print(x)
print(x[1])