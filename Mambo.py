p=1
while p != 'N':

    print("Choose a Horse : ")
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
        print('Go again')
        continue

    p = input('Would you like to continue? [y/N] : ')

    if (p=='N'):
         print('Thank you for Uma-ing with us')
         break
    
    elif(p=='y'):
         continue

    elif(p!='N' and p!='y'):
             print("We'll take that as a no")
             print('Thank you for Uma-ing with us')
             break
    
print('Mambo')
print('Hachimi')
print('WEI!')