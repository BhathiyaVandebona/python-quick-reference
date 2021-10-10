'''
Function will make your life more easy.
When use functions you can break a huge program
into smaller part and then implement them to complete the
program
'''

'''
this is how you declare a function
and it is a convention among python programmers to 
declare function in lowercase letters and if there are more than
one word use an undersroce inbetween words 
'''

def func():
    print("This is a function.")

def this_is_the_second_func():
    print("This is the second function.")

#passing parameters to functions
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

'''
you can pass more than one and any 
number of argumments 
to a function as long as
the function accept them
'''
#the return statement is used to return tht resultant value 
#of the function to the calling code this is done using the return statement
#return statement can also return mulitiple values
#any statement that comes after the return statement will not be exctuted

def concatenate(str_1,str_2):
    return str_1 + str_2

def multi_ret():
    return "ONE", "TOW"


#this is how you call a function
func() #this will call the function that is declared above

print("This is the factorial of 5 :" + str(factorial(5)))

returnvalueone,returnvaluetwo = multi_ret()
print(returnvalueone + " " + returnvaluetwo)
