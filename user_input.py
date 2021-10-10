#this function is used to get the factorial of a given number
def factorial(number):
    if number == 0:
        return 1
    else: 
        return number * factorial(number - 1)

#Using Python to read user inputs from the console
#Using the input() function

print("This will give the factorial of a given integer.")
usr_in = int(input("Enter an integer :")) #this is how you read an integer from the user 

#whenever we us the input() function the function will always return a string but if what you want is 
#an integer then you have to perform a type cast (keep that in mind)

print(f"The factorial of :{usr_in} is :{factorial(usr_in)}")


