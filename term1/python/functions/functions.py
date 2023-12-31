# def hello(name, age=28):
#     print(f'Hello, {name}! You are {age} years old!')
    
# def goodbye():
#     print('Goodbye!')

# #main
# goodbye()
# hello(name=input('What is your name? '))

TAX_RATE = 0.1
FLAT_SHIPPING = 10
#if something is a constant, by convention it should be in all caps

def add_tax(amount):
    return amount * (1 + TAX_RATE)

def add_shipping(amount):
    return amount + FLAT_SHIPPING

def calc_grand_total(amount):
    return add_tax(add_shipping(amount)) 

#main
subtotal = float(input('Subtotal: $'))
grand_total = calc_grand_total(subtotal)
print(f'Total: ${grand_total:.2f}') #the total has a formatting string