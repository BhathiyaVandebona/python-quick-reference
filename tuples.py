#reference -- >> https://docs.python.org/3/tutorial/datastructures.html?highlight=tuples

#this is an uneditable list (simply put) or immutable (cannot be modified or changed)
#tuples cannot be edited that is if you declared  tuple and that is it
#you cannot change it afterwards generally this data structure is used to store data that should not be changed
#or most likely will not change in the near future in the program

t1 = ("this is a tuple.", "This is the second index in the tuple.")

#to access the elements in the tuples
print(t1[0]) #this is also zero based indexed 
print(t1[1])

#you cannot add or remove elements form this tuple as well as you cannot change the elements as well

# t1[0] = "Cannot change" #you will get an exception

#can make lists of tuples or tuples of tuples as well
l1 = [("string", 90, True), (12, 34), (46,"Different data type")]
print(l1)

t2 = (t1, (32, False), ("Y", "HELLO"), ("Change", True, 78)) #just like lists a tuple can contain different types of data
print(t2)
