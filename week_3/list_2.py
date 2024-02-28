#
# Date :28/02/2024
# Name :xphlemy bosco
 
friends = ["Moghul","Jane","Ritah","Kamau","Njoroge", "mr bills"]

for friend in friends :
    print(friends)

    enemies = friends[:] #To copy one list into another
    print(enemies)

    fruits =["Guave","Mango","Apple","Banana","Pinaple","Kiwi"]

    # slice the list ie get part of the list
    print(fruits[0:3])

    del fruits[0]

    print(fruits)

    squares = [] #initializes an empty list

    for x in range (0,11):
        squares.append(x**2)

    print(squares)