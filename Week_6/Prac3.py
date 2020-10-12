class UnitConversion():
  def Conversion(self,x):
    print(x)
class MmToCm(UnitConversion):
  def Conversion(self,x):
    print("{} mm = {} cm".format(x,x*0.1))

class MmTometer(UnitConversion):
  def Conversion(self,x):
    print("{} mm = {} meter".format(x,x*0.001))

class CmTometer(UnitConversion):
  def Conversion(self,x):
    print("{} cm = {} meter".format(x,x*0.01))

class CmTomm(UnitConversion):
  def Conversion(self,x):
    print("{} cm = {} mm".format(x,x*10))

class meterTomm(UnitConversion):
  def Conversion(self,x):
    print("{} meter = {} mm".format(x,x*1000))

class meterTocm(UnitConversion):
  def Conversion(self,x):
    print("{} meter = {} cm".format(x,x*100))

obj1 = MmToCm()
obj1.Conversion(24)

obj2 = MmTometer()
obj2.Conversion(24)

obj3 = CmTomm()
obj3.Conversion(33)

obj4 = CmTometer()
obj4.Conversion(33)

obj5 = meterTomm()
obj5.Conversion(3)

obj6 = meterTocm()
obj6.Conversion(3)

