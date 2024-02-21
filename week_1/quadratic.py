# program to solve the quadratic equation
# Date :20/02/2024
# Name :Xphlemy Bosco
import math
a =float(input("Enter the coefficient of the first term : "))
b =float(input("Enter the coefficient of the second term : "))
c=float(input("Enter  the constnt "))



d =(float(b)**2) - 4 *float (a) *float(c) 
x_1 = (-b + math .sqrt(d) ) / 2* a
x_2 = (-b - math .sqrt(d) ) / 2* a

print("The solution of the quadratic equation is :" ,x_1 )
print("The solution of the quadratic equation is :" ,x_2 )