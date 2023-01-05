import math
class Circle:
    def CalculateArea(self):
        print("Enter Axis:")
        self.a=float(input())
        print("Enter Axis:")
        self.b=float(input())
        area=3.14*self.a*self.b
        print("Area of circle",(area))

    def CalculatePerimeter(self):
        Perimeter=2*3.14*math.sqrt((self.a*self.a+self.b*self.b)/2)
        print(Perimeter)


c=Circle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
