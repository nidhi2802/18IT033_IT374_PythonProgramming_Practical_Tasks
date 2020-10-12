def variable_length_func(*argv):
  for arg in argv:
    print(arg, end="#")

variable_length_func('One','Two','Three')
variable_length_func('One','Two','Three','Four','Five')
