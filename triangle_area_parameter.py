# Write a program to implement the triangle and return its parameter and area.

side1=float(input("Enter the first side of triangle:"))
side2=float(input("Enter the second side of triangle:"))
side3=float(input("Enter the third side of triangle:"))
class Triangle:
    def __init__(self,side1,side2,side3):
            self.side1=side1
            self.side2=side2
            self.side3=side3
            self.para=0
            self.area=0
    def para1(self):
        self.para=self.para+side1+side2+side3
        return self.para
    def area1(self):
        self.s=(self.para/2)
        self.area=self.area+(self.s*(self.s-side1)*(self.s-side2)*(self.s-side3))
        import math
        self.area=math.sqrt(self.area)
        return self.area
if(side1>0 and side2>0 and side3>0 and ((side1<side2+side3)and (side2<side1+side3)and (side3<side1+side2))):
   t=Triangle(side1,side2,side3) 
   t.para1()
   t.area1()
   print("The parameter of triangle is:",t.para,"unit")
   print("The area of triangle is:",t.area,"unit square")
else:
    print("Triangle is not form.")
