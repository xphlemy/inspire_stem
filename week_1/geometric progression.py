# This is a program to generate the terms and sum in geometric progression
# Date :20/02/2024
# Name Xphlemy Bosco

a =float(input("enter the first term"))
r =float(input("enter the common ratio"))
n =float(input("number of terms"))

term = a * (r**(n-1))
print("the term is",term)