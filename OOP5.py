
class computer:
    def __init__(self, CPU, Memory,radius,sideLength): ## CPU & Memory variable or attributes
        self.CPU=CPU
        self.Memory=Memory
        self.radius=radius
        self.sideLength=sideLength
    def config(self):
        print("config is CPU  " + self.CPU  +" & Memory " + self.Memory)

    def area(self):
        Area_circle=float(3.14*self.radius*self.radius)
        Area_square=float(self.sideLength*self.sideLength)
        print("The Area of circle is " + str(Area_circle), "The Area of square is "+str(Area_square))

comp1=computer("i5","8GB",5,7) 
comp2=computer("AMD","16GB",9,10)
comp1.config()
comp2.config()
comp1.area()
comp2.area()
