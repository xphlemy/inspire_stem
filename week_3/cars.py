# this is a program used to describe cars
# date: 28/02/2024
# name :xphlemy bosco

fav_car={"brand":"mazda demio","colour":"black","model":"cx","speed":"360km/h"}
print(fav_car)


print(fav_car["colour"])
print(fav_car["model"])
print(fav_car["speed"])

# to change the car values
fav_car["colour"] = "blue"
fav_car["speed"] ="430km/h"
fav_car["model"] = "G- wagon 4"
print(fav_car)

fav_car["size"] ="570mm x 1852mm x 1443mm"
print(fav_car)

del fav_car["model"]
print(fav_car)


for key,value in fav_car.items() :
    print(key)
    print("\n")
    print(value)