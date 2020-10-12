inp_celcius = float(input("Enter temperature in Celcius "))
inp_fahrenheit = float(input("Enter temperature in fahrenheit "))
cel_to_fah = (inp_celcius*1.8)+32
print(inp_celcius, " celcius is equal to ", cel_to_fah, " fahrenheit")
fah_to_cel = (inp_fahrenheit-32)*(5/9)
print(inp_fahrenheit, " fahrenheit is equal to ", fah_to_cel, " celcius")