import math  # Necesario para la función de raíz cuadrada
from decimal import Decimal

# Exercise 1
one_list = [21, 22, 23]
one_tuple = (41, 51, 61)
one_float = 3.14
one_integer = 7777
one_decimal = Decimal(2.5) # Utilizando Decimal del módulo decimal
one_dict = {
    'a': 1000, 
    'b': 2000, 
    'c': 3000
}

# Exercise 2
rounded_float = math.ceil(one_float)
print("Rounded Float:", rounded_float)
#Output = Rounded Float: 4

# Exercise 3
sqrt_float = math.sqrt(one_float)
print("Square Root of One Float:", sqrt_float)
#Output = Square Root of One Float: 1.772004514666935

# Exercise 4
first_dict_element = one_dict['a']
print("First Element from One Dictionary:", first_dict_element)
#Output = First Element from One Dictionary: 1000

# Exercise 5
second_tuple_element = one_tuple[1]
print("Second Element from One Tuple:", second_tuple_element)
#Output = Second Element from One Tuple: 51

# Exercise 6
one_list.append(24)
print("List after Adding an Element to the end of one list:", one_list)
#Output = List after Adding an Element to the end of one list: [21, 22, 23, 24]

# Exercise 7
one_list[0] = 100
print("List after Replacing First Element:", one_list)
#Output = List after Replacing First Element: [100, 22, 23, 24]

# Exercise 8
one_list.sort()
print("Sorted List Alphabetically:", one_list)
#Output = Sorted List Alphabetically: [22, 23, 24, 100]

# Exercise 9
one_tuple += (71,)
print("Tuple after Reassignment:", one_tuple)
#Output = Tuple after Reassignment: (41, 51, 61, 71)
