class Rectangle:
    def CalculateArea(self):
        print("Enter length:")
        self.l=float(input())
        print("Enter breadth:")
        self.b=float(input())
        area=self.l*self.b
        print("Area of rectangle",(area))

    def CalculatePerimeter(self):
        Perimeter=2*(self.l*self.b)
        print(Perimeter)


c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
