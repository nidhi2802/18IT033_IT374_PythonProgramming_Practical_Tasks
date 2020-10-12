def areaCircle(radius):
    pi = float(3.14)
    area = pi*radius*radius
    print("Area of circle with radius ", radius, " is ", area)

def areaSquare(length):
    area = length*length
    print("Area of square with length ", length, " is ", area)

def areaRectangle(length, breadth):
    area = length*breadth
    print("Area of rectangle with length ", length, " and breadth ", breadth, " is ", area)

def areaTriangle(altitude, base):
    area =0.5*altitude*base
    print("Area of triangle with altitude ", altitude, " and base ", base, " is ", area)

radius = 2.5
length = 2
breadth = 4
altitude = 3
base = 4
areaCircle(radius)
areaSquare(length)
areaRectangle(length, breadth)
areaTriangle(altitude, base)