

# Positional arguments are passed to the function based on the order of position
# Keyword arguments are passed into the function by explicitly specifying the name of each argument
# Default arguments are defined in the function
def year_of_birth(name, age):
    year = 2023 - age
    print(f'Hello {name}, your were born in {year}')

def my_country(country = 'Kenya'):
    print(f'Hello you are from {country}')

# To use a function that accepts any number of arguments we use a star before parameter
def hello(*names):
    for name in names:
        print(f'Hello, {name}')

def sum(*nums):
    result = 0
    for num in nums:
        result += num
    return result

# 
def multiply_many(**kwargs):
    result = 1
    for num in kwargs.values():
        result *= num
    return result
# Assignments

def concatenate_args(*strings):
   joins = ''
   for string in strings:
    joins = joins +' '+ string
   return print(joins)

def concatenate_kwargs(**kwargs):
    joined_string = ''
    for string in kwargs.values():
        joined_string = joined_string + ' ' + string
    return print(joined_string)

concatenate_kwargs(a = 'Banana', b = 'grey')