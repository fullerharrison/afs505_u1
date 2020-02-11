# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog has-a object of "Animal"
class Dog(Animal):

    def __init__(self,name):
        ## __init__ is-a object with two arguements
        self.name = name

## Cat has-a object "Animal"
class Cat(Animal):
    def __init__(self, name):
        ## __init__ is-a object with two arguements
        self.name = name

## is-a object with one arguements
class Person(object):
    ## has-a object
    self.name = name

    ## Person has-a pet of some kind
    self.pet = None
## is-a object of person
class Employee(Person):
    def __init__(self, name, salary):
        ## has a 2 arguement object
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## is a object class
class Fish(object):
    pass

## is-a object class
class Salmon(Fish):
    pass

## is a object class
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## marry has-a pet satan
marry.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet roveer
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a fish
harry = Halibut()
