class Square:
    def CalculateArea(self):
        print("side of square:")
        self.s=float(input())
        area=self.s*self.s
        print("Area of square",(area))

    def CalculatePerimeter(self):
        Perimeter=4*(self.s)
        print(Perimeter)


c=Square()
x=c.CalculateArea()
y=c.CalculatePerimeter()
