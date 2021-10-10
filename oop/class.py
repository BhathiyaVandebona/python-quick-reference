#classes are user define data types that allows us to map real world entities into datatypes that we can manipulate

#this is how to create a simple class
# class is a like a mold or a template out of this you can model actual objects
class Employee:
    #the builtin datatypes are used to represent attribute of the employee
    #here the slf must always be the first parameter of the parameter list
    def __init__(self, name, age, address, gender, branch, emp_type):#this is known as an initialize function and it is like a constructor in Java
        #the variables given inside of the parathensis acts as attributes of this class
        #self is like the this key word in Java or this-> in cpp this means it is refering to the current object
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.branch = branch
        self.emp_type = emp_type
    
    #this is a class function
    def details(self):# here the slef is a must because an argument is passed by default to check this remove the self and give this a try
        print("The name of the employee is :"+self.name)
        print("The age of the employee is :"+str(self.age))
        print("The address of the employee is :"+self.address)
        print("The gender of the employee is :"+self.gender)
        print("The branch of the employee is :"+self.branch)
        print()


#this is the actual object or the instance
e1 = Employee("John", 40, "Address", "M", "NEW", "PROGRAMMER")
#here you don't have to pass a value to the self parameter it is automatically referred
#to access the atributes in this object

print("The name of the employee is :"+e1.name)
print("The age of the employee is :"+str(e1.age))
print("The address of the employee is :"+e1.address)
print("The gender of the employee is :"+e1.gender)
print("The branch of the employee is :"+e1.branch)
print("The emp_type of the employee is :"+e1.emp_type)

#and you can create as much employees from this template
#you can even assign e1 another new employee object as well

e1.details()
