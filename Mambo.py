print("Choose a Horse :")
print('a.) Matikanetannhauser')
print('b.) Tokai Teio')
print('c.) Daitaku Helios')
uma = input("Choice [a, b, c] : ")

if (uma=='a'):
    y = int(input("How Much? : "))

    for i in range(y):
        print("MAMBO")
elif (uma=='b'):
    y = int(input("How Much? : "))

    for i in range(y):
            print("Hachimi")
elif (uma=='c'):
    y = int(input("How Much? : "))

    for i in range(y):
            print("WEI!")
else:
     print("What?")