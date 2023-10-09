# x = int(input('What is X? '))
# y = int(input('What is Y? '))

# if x < y:
#         print('x is less than y')    
# elif x > y:
#         print('x is greater than y')
# else:
#         print('x is equal to y')


# score = int(input('Score: '))

# if score >= 90:
#     print('High Distinction')

# elif score >= 80:
#     print('Distinction')

# elif score >= 70:
#     print('Credit')

# elif score >= 50:
#     print('Pass')

# else:
#     print('Failed')

# name = input('What is your name? ')

# match name: 
#     case 'Harry' | 'Ron' | 'Hermione':
#         print('Gryffindor')

#     case'Draco':
#         print('Slytherin')

#     case _:
#         print('Mudblood!')


import math

choice = input("Please enter a shape, either square, circle or triangle: ")

match choice.lower():
    case "square":
        s = float(input("Please enter the length of one of the sides: "))
        print (f"The area of your square is {round(s ** 2, 2)} units")
    case "circle":
        r = float(input("Please enter the radius of the circle: "))
        print (f"The area of your circle is {round(((math.pi * r) ** 2), 2)} units")
    case "triangle":
        b = float(input("Please enter in the base length of your triangle: "))
        h = float(input("Please enter in the height of your triangle: "))
        print (f"The are of your triangle is {round((0.5 * b * h), 2)} units")
    case _:
        print ("That is not a valid shape, please try again.")