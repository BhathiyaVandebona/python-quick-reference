#while loops and for loops in python

#this is a simple while loop
index  = 1
while index < 11: #as long as this condition is true the indented block will be executed (this is the loop condition)
    print("index is :" + str(index))
    index += 1

#this is a simple for loop
#in python you can use for loops to loop over collections
#even strings

s1 = "This is a string."

print()
index = 0
for letter in s1:
    print("The character at index :" + str(index) + " is :" + letter)
    index += 1

print()
#this is looping over a list
l = ["Jordan", "Kevin", "Locelso", "Sterling"]

for name in l:
    print(name)

print()
#to go through a range of numbers use
for i in range(10): #starts from zero
    print(i)

print()
for i in range(2,10): #starts from 2 amd will go upto 9
    print(i)

print()
for i in range(2,10,2): #starts from 2 amd will go upto 8 from 2 by 2 2,4,6,8
    print(i)


