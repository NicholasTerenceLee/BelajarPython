x = float(input("What's your score? : "))

if (x>=90 and x<=100):
    print("A , Great Job")
elif (x>=80 and x<90):
    print("B , Nice Try")
elif (x>100):
    print("What the hell")
elif (x<0):
    print("How?")
else:
    print("C , Too bad, try harder next time")
