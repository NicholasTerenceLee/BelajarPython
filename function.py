def mambo(honse):
    x=0
    while x != (honse + "!"):
        x = input("How " + honse + " are you today? : ")

        if (x==honse +"!"):
            print("You are " + honse + "!")
            break
        else:
            print("You are not " + honse + " enough!")
            continue
    print('Mambo')

x = input("What honse are you? : ")

print("Mambo")
mambo(x)

