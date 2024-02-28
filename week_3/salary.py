#
# Date :26/02/2024
# Name :xphlemy bosco


salary = int(input("Enter current salary"))
if salary < 100000 :
    salary = 1.3 * salary
    print("New salary is :" ,salary)
elif salary > 100000 and salary < 150000 :
    salary = 1.5 * salary
    print("New salary is :" ,salary)
elif salary > 150000 :
    salary = 1.05 * salary
    print("New salary is :" ,salary)
    
