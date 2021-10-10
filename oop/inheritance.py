class Employee:
    #the builtin datatypes are used to represent attribute of the employee
    def __init__(self, name, age, address, gender, branch, emp_type):#this is known as an initialize function and it is like a constructor in Java
        #the variables given inside of the parathensis acts as attributes of this class
        #self is like the this key word in Java or this-> in cpp this means it is refering to the current object
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.branch = branch
        self.emp_type = emp_type

    def details(self):# here the slef is a must
        print("The name of the employee is :"+self.name)
        print("The age of the employee is :"+str(self.age))
        print("The address of the employee is :"+self.address)
        print("The gender of the employee is :"+self.gender)
        print("The branch of the employee is :"+self.branch)


class Hunter(Employee): #now this is a sub class of the super class Employee
    
    #here you get access to all the super class atributes as well as the class methods
    def __init__(self, name, age, address, gender, branch, emp_type, experience):#this is known as an initialize function and it is like a constructor in Java
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.branch = branch
        self.emp_type = emp_type
        self.experience = experience
        
    #along with functions or attributes that are unique to this subclass    
    def get_experience(self):
        return self.experience


e1 = Employee("John", 40, "Address", "M", "NEW", "PROGRAMMER")

te1 = Hunter("John Wick", 45, "Confidential", "M", "New York", "Hunter", 30)

e1.details()
print()
te1.details()
print()
print(te1.name + " year of experience :" + str(te1.get_experience()))
