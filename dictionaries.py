'''
refernce -->> https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionaries

if you want a data structure to store key value pairs then this is it
here each key must be unique the key is used as the identifier to identify 
a pair and the key can be of any data type as longa as they are unique
'''

#creating a dictionary
d1 = {
        "Jan": 31, 
        "Feb": 28,
        "Mar": 31,
        "Apr": 30,
        "May": 31,
        "Jun": 30,
        "Jul": 31,
        "Aug": 31,
        "Sep": 30,
        "Oct": 31,
        "Nov": 30,
        "Dec": 31,
     }

#here each key is associated iwth a value

#to access 
print(d1) #this will print the dictionary

#use the key to access elements in the dictionary
print(d1["Jan"])

#you can also use this
print(d1.get("Aug","This doen't exist")) #when you are using this get function you can define a default value to output of the key mention doesn't exist

print(d1.get("none","This doen't exist"))
