def ciggs():
    x = int(input("How much? : "))
    x2 = float(x* 25000)
    return x, x2
def ber():
    y = int(input("How much? : "))
    y2 = float(y* 10000)
    return y, y2
def light():
    z = int(input("How much? : "))
    z2 = float(z * 15000)
    return z, z2

shops = {
    "Cigarettes": 25000, 
    "Beer": 10000, 
    "Lighter" : 15000
}
x = 0
y = 0
z = 0
a = "Cigarettes"
b = "Beer"
c = "Lighter"
print("Here's a list of the items : ")
for key, value in shops.items():
    print(key,": Rp", value)

l = 0
price = 0
while l != "N":
    print('Which item would you like to choose? ')
    print("a.) Cigarettes")
    print('b.) Beer ')
    print("c.) Lighter")
    choice = input("Choice : ")

    if choice =="a":
        x, x2 = ciggs()
        price += x2

    elif choice == "b":
        y, y2 = ber()
        price += y2

    elif choice == "c":
        z, z2 = light()
        price += z2

    else:
        print("Try Again")
        continue

    l = input("Would you like to add more? [y/N] : ")

    if l =="y":
        print("Alr")
        continue
    elif l =="N":
        print("Alr")
        break
    
shops.update({"Cigarettes" : x})
shops.update({"Beer" : y})
shops.update({"Lighter" : z})
if x == 0:
    shops.pop("Cigarettes")
if y == 0:
    shops.pop("Beer")
if z == 0:
    shops.pop("Lighter")

print("Here's the list of items you bought : ")
for key, value in shops.items():
    print(key , "   ---    Quantity : ", value) 
print(f"Your total price is : Rp  {price}")




