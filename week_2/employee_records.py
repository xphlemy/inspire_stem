# Program to show the employee records
# Date 21/02/2024
# Name : Collins Bosco

name = input("Enter name of the employee :")
age = input("Enter age of employee :")
salary = int(input("Enter salary of employee :"))
bonus = int(input("Enter bonus of employee :"))

inc = 140/100
new_salary =(salary * inc)
print("The new salary is",new_salary)

dec = 7000
new_bonus = (bonus - dec)
print("The new bonus is",new_bonus)