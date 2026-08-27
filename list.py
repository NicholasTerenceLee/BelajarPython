fruit = ['Apple', 'Banana', 'Cherry', 'Strawberry', 'Pineapple']
data = ['Apple', 'RED', 'ROUND!', 5]

print(fruit)
print(fruit[-2])

fruit.insert(3, 'Mango')
print(fruit)
print(fruit[-2])

fruit.append('Orange')
print(fruit)
print(fruit[-2])

fruit.append('Grape')
print(fruit)
print(fruit[-2])

fruit.insert(3, 'Watermelon')
print(fruit)
print(fruit[-2])

fruit[1] = 'Blackcurrent'
print(fruit)
print(fruit[-2])

fruit.remove('Apple')
print(fruit)
print(fruit[-2])

fruit.pop(-2)
print(fruit)
print(fruit[-2])