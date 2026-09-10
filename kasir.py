def calc(x):
    quant = int(input("How much? : "))
    money = float(x*quant)
    return money, quant

shops = {
    'item': {
        "Cigarettes": 25000, 
        "Beer": 10000, 
        "Lighter" : 15000
    },
    "totalitems": {
    }

}


a = "Cigarettes"
b = "Beer"
c = "Lighter"
print("Here's a list of the items : ")
for key, value in shops['item'].items():
    print(key,": Rp", value)
i = 0
it = 0
ite = 0
l = 0
price = 0
while l != "N":
    quant = 0
    print('Which item would you like to choose? ')
    print("a.) Cigarettes")
    print('b.) Beer ')
    print("c.) Lighter")
    choice = input("Choice : ")

    if choice =="a":
        money, quant = calc(25000)
        i += quant
        shops['totalitems'].get("Cigarettes")
        shops['totalitems'].update({"Cigarettes" : i})

    elif choice == "b":
        money, quant = calc(10000)
        it += quant
        shops['totalitems'].get("Beer")
        shops['totalitems'].update({"Beer" : it})

    elif choice == "c":
        money, quant = calc(15000)
        ite += quant
        shops['totalitems'].get("Lighter")
        shops['totalitems'].update({"Lighter" : ite})

    else:
        print("Try Again")
        continue

    price += money

    l = input("Would you like to add more? [y/N] : ")

    if l == "y":
        print("Alr")
        continue
    elif l == "N":
        print("Alr")
        break

print("Here's the list of items you bought : ")
for key, value in shops['totalitems'].items():
    print(key , "   ---    Quantity : ", value) 
print(f"Your total price is : Rp  {price}")
