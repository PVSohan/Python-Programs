class Cars:
    def __init__(self,colour,car_type,price,Name):
        self.colour =colour
        self.car_type = car_type
        self.price = price
        self.Name = Name
    def display(self):
        print(f"The colour of the car is :{self.colour}")
        print(f"The type of the car is :{self.car_type}")
        print(f"The price of the car is :{self.price}")
        print(f"The Name of the car is :{self.Name}")
Cars1 = Cars("Red","Convertible","10 Lakh","Pugo")
Cars1.display()
Cars2 = Cars("Blue","Sedan","6 Lakh","Mavo")
Cars2.display()
