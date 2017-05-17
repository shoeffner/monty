# Class without anything
class Person:
    pass

print(Person)


# Instantiate
person = Person()
print(person)


# Class with constructor
class Person:

    def __init__(self, name, age, height):
        pass


# Assign variables to objects:
person1 = Person('Alecia', 37, 1.63)  # note the missing "self"!
person2 = Person('Ronald', 43, 1.73)


# Class with constructor and member variables to store
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


# Assign variables and access them
person1 = Person('Alecia', 37, 1.63)  # note the missing "self"!
person2 = Person('Ronald', 43, 1.73)
print(person1.name)
print(person2.name)
print(person1.name, person1.age, person1.height)


# Method
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        return 'Hi, I am ' + self.name

person1 = Person('Alecia', 37, 1.63)
person2 = Person('Ronald', 43, 1.73)
print(person1.introduce())
print(person2.introduce())


# Note that the dot notation is really just convenience:
# This makes it a little clearer, why we leave it out when calling the
# functions on the objects, as well why we need it.
print(Person.introduce(person1))
