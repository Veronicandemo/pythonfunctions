#reusable block of code that optionaly accepts some inputs, does some work(computation) and optionaly returns an output
## Use of def key word  to create...def means define followed by the function name
### followed by parantesis that have optional inputs...followed by colon
#### then the body off the function that is idented below the function -- to define the scope of the function
##### optional return input
#####  to run a function you have to invoke it, calling it
## __init__.py signifies that that the dir is a python package
## A module is a file that contains python code

##Function naming convention
### cannot start with a number
### cannot contain a space
### A function name should be in lower case
### A function name should be descriptive of what the funvtion does
## If it  has two words combone them using underscore

###The Return keyword
##Return the value and ends the function
##The return keyword if optional in pyrhon functions
def helloworld(name): 
        print(f"Hello {name}")
    
# helloWorld("Veronica")
# helloWorld("World")
# helloWorld("Hopper")

def welcome(school, student):
        print(f"Hello {student}, Welcome to {school}")

