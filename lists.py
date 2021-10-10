#this is a built-in data structure in Python
#this is similar to a dyanmic array (for me) 
#without the restriction of adding data of the 
#same type 
#reference -- >> https://docs.python.org/3/tutorial/datastructures.html?highlight=list

# declaring a list is as follows variable_name = [] this will declare an empty list
l1 = ["This is a string", 12, True, ["This is a list inside of the list", 20]] #you can add any type of data to this list

l2 = ["Kevin", "David", "Mike", "Jim"]

#indexing starts at zero (zero based indexing) 
#to access an element in the list as follows
index_0 = l2[0]

#and you can do this as well
index_3 = l2[-1] #this will give the last element in the list
print(index_3)
index_2 = l2[-2] 
print(index_2)
index_1 = l2[-3] 
print(index_1)
index_0 = l2[-4]# and so on until the beginning of the list
print(index_1)

#to select from an index upto an index
print(l2[1:3])#this will get all the elements from 1 upto 2 but not the 3rd element

#to modify an element you can do this 
index_0 = "Nathan" #this will set the element at the index zero to Nathan

print(index_0)

#list functions
#you can print a list using the print function
print(l2) #output -->> [...content...]

#the extend() function will append a list to another list
l3 = ["Jack","Foden","Walker"]
l3.extend(l2)
print(l3)

#the append() function will add a new element to the end of the list
l2.append("Anderson")
print(l2)

#to add an element to a given index use the insert function
l4 = ["Jordan", "Kevin", "Locelso", "Sterling"]
l4.insert(2,"Mahrez")
print(l4)

#to remove an element from the list use
l4.remove("Locelso") #list_reference.remove("ELEMENT_TO_BE_REMOVED")

#to remove all the elements from the list use 
l4.clear() #this will remove all the elements in the list (empty the list)

#the pop() function will remove the last element
l4 = ["Jordan", "Kevin", "Locelso", "Sterling"]
l4.pop() #this will remove the last element

#to get the index of an element use the 
print("This is the index of jordan ::"+str(l4.index("Jordan")))
#if the element doesn't exist then it will give an exception

#to get the count of a certain element use
print(l4.count("Jordan")) #this will return the number of time an element is repeated

#to sort the list use
l4.sort()
print(l4)

#to reverse a list use reverse()
l4.reverse()
print(l4)

#to copy a list use 
l5 = l4.copy()
print(l5)



