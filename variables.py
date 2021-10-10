#you can just declare variabels which will act as a container to 
#store values of different types as well as the same type
#some basic data types in python[3] are as follows

    #1. STRING
    #2. INTEGER
    #3. FLOATING-POINT NUMBERS (FRACTIONS)
    #4. BOOLEAN (True or False)

#in python you don't have to specify the data type when you 
#declare the variables in python the interpreter will do the 
#work for you

variable_string = "This is a string variable"

variable_integer = 100 #this is an integer variable

variable_float = 23.89 #this is a floating point variable

#accessing the varibales can be done as follows
print(variable_string)
print(variable_integer)
print(variable_float)

variable_integer = 1200 + variable_integer * 2

print(variable_integer)

name = "Your name"
age = 70

print("The name of the person is " + name + ".") #this is known as string concatenation
print(f"The age is :{age}.")#this is know as the f string it can be used to format strings
