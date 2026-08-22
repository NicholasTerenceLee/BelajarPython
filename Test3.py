n=1
while (n != 'N'): 

    print("Finding the Area of a Triangle")

    x = float(input("What's the Height of the Triangle : "))
    y = float(input("What's the Base of the Triangle : "))

    z = x*y/2

    print(f"The Area is : {z}")

    n = input('Continue? [y/N] : ')

    if (n == 'N'):
        print("Thank you for using this program")
        break
    elif (n == 'y'):
        print("Here you go")
        continue
    else:
        print("We'll take that as a no")
        print('Thank you for using this program')
        break




    
