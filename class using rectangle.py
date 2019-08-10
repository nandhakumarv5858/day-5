class Rectangle:
    def __init__(self,l,w):
        self.lengh =l
        self.widht =w
    def Rectangle_area(self):
        print(self.lengh*self.widht)
a=int(input("Enter lenght"))
b=int(input("Enter widht"))
Rect1=Rectangle(a,b)
Rect1.Rectangle_area()
