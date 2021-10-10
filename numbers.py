#to add get access to more functions use
from math import * #this means import all the functions from the math module

#for reference -->> https://docs.python.org/3/library/math.html there are more 
#functions provided by Python than the once that are given here


print(540000) #this will print the 54000 integer on to the console

#you can use positive as well as negative number in python

neg = -90.34
pos = 90.34

print("This is a positive number :" + str(pos))
print("This is a negative number :" + str(neg))

#you also perform arithmatic operations as follows

print(45 + 67)
print(54 - 36)
print(54 % 36) #modulus operator will divide 54 by 36 and will return the remainder eg : 54 % 36 = 18
print(54 * 36) #multiplication

print(2 ** 3) #this is the raise to the power operator will output 8

#to type cast a number to a string use
print("this is a string now ::" + str(neg))#otherwise this operation is not possible in python

#there are lots of mathematical functions as well.

print(abs(neg)) #this abs() function will return the absolute value of the neg that is : 90.34
print(pow(2,3)) #this function is used to raise some number to a power just like the ** operator did 
#(here the first argument is the number and the second argument is the power) 

maximum = max(34,100) #this will return the maximum value of the two given
minimum = min(34,100) #this will return the minimum value of the two given

rounded_pos = round(pos) #this will round the given number (follows standard rounding rules)

