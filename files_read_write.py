#to open a stream use this 
#====================================================================
#reading a file
text_file = open("text_file.txt", "r+") 

#file open modes are as follows
#1. r -->> read
#2. w -->> write
#3. a -->> append (you can aoppend info to the end of the file)
#4. r+ -->> read and write

#reading the file
# to check whether the file is readable use this
print(text_file.readable())#return a boolean value

#to read the whole file use this
print(text_file.read())

#to read a line from the file use this
print(text_file.readline())#this will read an individual line this will move the virtual head to the start of the second line

#to get a list of all the lines in the text file use
print(text_file.readlines())

for line in text_file.readlines():
	print(line)

#after you are done with the file you have to close the stearm as well
text_file.close()

#====================================================================
#writing to a file


text_file = open("text_file.txt", "a") 


#this is how you can write to a file
text_file.write("PYTHON IS EASY.\n")#this will not append a newline character to the end of the string by defalut so we have to do that maually

text_file.close()
