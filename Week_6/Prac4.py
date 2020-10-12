from abc import ABC, abstractmethod
class Shape(ABC):
  @abstractmethod
  def area(self, side1, side2):
    pass

class Triangle(Shape):
  def area(self, side1, side2):
    print("Area of Triangle is: ",0.5*side1*side2)

class Rectangle(Shape):
  def area(self, side1, side2):
    print("Area of Rectangle is: ",side1*side2)

R = Triangle() 
R.area(3,4)

RT = Rectangle() 
RT.area(3,4)
