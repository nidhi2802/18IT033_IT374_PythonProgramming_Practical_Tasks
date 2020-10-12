n = int(input("Enter number to print Fibonacci Series: "))
class ErrorInCode(Exception):
  def __init__(self, data):
    self.data = data
  def __str__(self):
    return repr(self.data)

series = []
series.append(1)
series.append(1)
try:
  if n>100:
    raise ErrorInCode(100)
  elif n == 0:
      print("Fibonacci Series with n=0 does'nt exist")
  elif n == 1:
      print("Fibonacci Series with n=1: ", series[0])
  else:
      [series.append(series[k - 1] + series[k - 2]) for k in range(2, n)]
      print("Fibonacci Series with n={}: {}".format(n,series))

except ErrorInCode as ae:
  print("More than {} is not allowed!!!!".format(ae.data))
 