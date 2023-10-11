from my_module import foo, person, x
import my_module
from colort import colorize, ForegroundColor as fc, Style



# print(dir(my_module))

foo(person)
foo({'name': 'Anya', 'age': 28})

print(x)

colored_text = colorize('Hello World!', fc.GREEN, Style.BOLD)
print("colored text: ", colored_text)