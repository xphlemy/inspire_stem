# strings in python
# Date 22/02/2024
# Name : Xphlemy Bosco

city ="nairobi"

print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[5]) #b
print(city[6]) #i

# convert to uppercase


print(city)
print("\n") # print a new line
print(city.upper())
name = "XPHLEMY BOSCO"
print(name)
print(name.lower()) # convert strings to lower case

town = "       Naivasha    "
print("\t") # new tab
print(town.strip())

# add two strings

f_name ="Xphlemy"
s_name ="Bosco"

full_name = f_name + s_name

print(full_name)

#replacing a character

fruit ="Orange"

print(fruit.replace("O","Y"))

subject = "Phsical:Sciences"

print(subject.split(":"))

age = 20
height = 1.6

print("I am  {0} years old  and {1} meters tall"  .format(age,height))

activity ="dancing"
print(" My hobby is %s" %(activity))
name = "xphlemy"
print(len(name))

print(f"My full name is {name}")

height = 1.2333484
print("My height is  %5.4f"%(height))