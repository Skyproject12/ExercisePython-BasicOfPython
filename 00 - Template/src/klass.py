class Person : 
    name = None 
    age = None

    # make constructor
    def __init__(self, name, age): 
        self.name = name 
        self.age = age  

    # setter name 
    def say_name(self): 
        print('My name is %s' % self.name) 

    # set age 
    def say_age(self): 
        print('My age is %s' % self.age)