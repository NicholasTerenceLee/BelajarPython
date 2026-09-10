class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print('Your car is : ', self.brand)


x = input("What is your car ? : ")

p1 = Car(x)

p1.show()
        

