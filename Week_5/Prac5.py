def make_multiplier_of(limit=10):
  def multiplier(x):
    output=[]
    for i in range (1,limit+1):
      output.append(x*i)
    return output
  return multiplier

table_of = make_multiplier_of() # Default limit
print(table_of(3))
table_of = make_multiplier_of(5) # Modified limit
print(table_of(5))