'''
we can use if else statements to control the flow of a prgram
if the condition is true then the code under the if block will be executed 
otherwise will move to the else block and will execute it 
the else statement is not mandatory for the if statement but not vise versa 
'''

def feactorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

#not function will invert the values ex: True to False and vice versa
# and the 'and' is like the && operator in C
# and the 'or' is like the || operator in C

def demo(is_raining: bool, goto_beach: bool)->None:
    if not(is_raining) and goto_beach:
        print("It is not raining and we are going to the beach.")
    elif not(is_raining) and not(goto_beach):
        print("It is not raining but we are not going to the beach.")
    elif is_raining and goto_beach:
        print("It is raining but we are going to the beach.")
    else:
        print("It is raining and we are not going to the beach.")

demo(True, False)

'''

comparison opeartors
=====================
1. > greater than 
2. < less than
3. >= greater than or equal
4. <= less than or equal
5. == equality
6. != not equal

you can compare numbers as well as strings 
using comparison operator given here
'''

def find_max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

print(find_max(23, 34.8))
