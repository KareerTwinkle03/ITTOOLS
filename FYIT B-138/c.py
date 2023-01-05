class Circle:
    def CalculateArea(self):
        print("Radius of circle:")
        self.r=float(input())
        area=3.14*self.r*self.r
        print("Area of circle",(area))

    def CalculatePerimeter(self):
        Perimeter=2*3.14*self.r
        print(Perimeter)


c=Circle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
