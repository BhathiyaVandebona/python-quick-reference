#this is how you can stop the interpreter from breaking the executuion
# use this to read more on this -->> https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception

usr_in = None

def read_input():
    #this is only used to read numbers from the console
    try:
        sur_in = int(input("Enter an integer:"))
    #in python it is convention to use the specific exception in the except _______:
    except ValueError:
        print("You enter an invalid input")
    except:#this is a default catch block this will catch any exception that might occur
        print("An exception occured.")
    #if the user input is not a valid number then
    #the interpreter will stop the execution of the program
    # to prevent this we use try except

def factorial():
    if usr_in == 0:
        return 1
    else:
        return usr_in * factorial(usr_in - 1)


