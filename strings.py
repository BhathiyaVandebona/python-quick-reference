#form more information -->> https://www.tutorialspoint.com/python/python_strings.html

#any plain text can be used as a string
#to declare a string you need to use 
# " " two quotation marks in between you can 
#include the string or the text that your need to have

this_is_a_string = "This is the content"

phrase = "Python is easy"

print(phrase)

#this is string concatenation (appending strings to other strings)

phrase_2 = phrase + " to learn." # this will append the " to learn." at the end of the phrase.

print(phrase_2)

#using string functions [for more information -->> https://www.programiz.com/python-programming/methods/string]

print(phrase_2.lower()) #converts the whole string in to lower case and will return that string without altering the original string
print(phrase_2.upper()) #converts the whole string in to upper case and will return that string without altering the original string

phrase_2 = phrase_2.upper()

print("this function checks whether the string is in lowercase :" + str(phrase_2.islower()))

print("this function checks whether the string is in uppercase :" + str(phrase_2.isupper()))

print(phrase_2)

#to get the lenght of the string use the len()
print("the length of the string (number of characters in the string) is :" + str(len(phrase_2)))

#you can also use the array notaion to access characters in the string
print(phrase_2[3])#this will print the character at the index three (indices starts from zero)

phrase_2 = phrase_2.lower()
#you can use this function to get the index where the first character of a substring or a character starts (returns an integer)
print(phrase_2.index("e"))# if the substring is not found the interpreter will throw an exception

#replace any substring in the string you want using this
print(phrase_2.replace("easy","super easy"))#this will replace easy to super easy

