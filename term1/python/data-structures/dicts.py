my_cat = {'name' : 'Paarthurnax', 'age' : '1', 'colour' : 'white'}

# print(my_cat['age'])

# cats = [
#     {'name' : 'Paarthurnax', 'age' : '1', 'colour' : 'white'}
#     {'name' : 'Alduin', 'age' : '2', 'colour' : 'Black'}
# ]

# print(cats[0]['name'])

# print('Paarthurnax' in my_cat.values()) #prints true or false if it's a value in the list
# print(my_cat.values()) #prints values of my_cat
# print(my_cat.keys()) #prints keys of my_cat
# print(my_cat.items()) #returns a list of tuples containing two values

# this for loop visits each element in the list and executes the print 
# for k, v in my_cat.items(): #k is key and v is value
#     print(f'The value of "{k}" is {v}')

print(my_cat.get('state', 'Unknown'))