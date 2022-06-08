## Animal is-a object (yes, sort of confusing)
class Animal(object):
    pass

##Dog is-a Animal

class Dog(Animal):

    def __init__(self, name):

        #Dog has-a name attribute
        self.name = name

#Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        #cat has-name attribute
        self.name = name

#Person is-a object
class Person(object):

    #person has-a name and pet

    def __init__(self, name):

        self.name = name

        self.pet = None


#An employee is-a person
class Employee(Person):

    #an employee has-a name and salary

    def __init__(self, name, salary):

        #inherits the parent class (Person) name attribute
        super(Employee, self).__init__(name)

        self.salary = salary

#Fish is-a object
class Fish(object):
    pass

#Salmon is-a object
class Salmon(object):
    pass

#Halibut is-a Fish
class Halibut(Fish):
    pass


#rover is an instance of the Dog class and the name attribute is given a value of "Rover"
rover = Dog("Rover")

#satan is an instance of the Cat class and the name attribute is given a value of "Satan"
satan = Cat("Satan")

#mary is an instance of the Person class and the name attribute is give a value of "Mary"
mary = Person("Mary")

#The instance of Mary has an attribute of pet that is assigned a value of the instance of Cat called satan
mary.pet = satan

#frank is-a instance of employee given a name of Frank and a salary of 120000
frank = Employee("Frank", 120000)

#The frank object's pet attribute is assigned a value of rover
frank.pet = rover

#flipper is-a instance of the Fish class
flipper = Fish()

#crouse is-a instance of the Salmon() class
crouse = Salmon()

#harry is-a instance of the Halibut() class
harry = Halibut()