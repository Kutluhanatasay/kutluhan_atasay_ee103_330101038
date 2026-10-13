import math 

x = float(input("ENTER X TO FİND THE CUBE ROOT OF?:"))

g = float(input("WHAT GUESS TO START WİTH?"))


error = g**3 - x

ng = g - (g**3 - x)/(3 * g**2) 
print(error)
print(ng)
