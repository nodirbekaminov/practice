""" CLASS
(1). What is Class.
(2). Ordinary and static properties.
(3). Special methods.
"""

print("====== What is class =====")
# Class => blueprint for object creation
# Structure => State, Constructor, Methods


class Person():
    # State
    message = "Class state properties"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Mehtods

    def introdcue(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says I'm {self.age}")


person = Person("Nick", 26)
person2 = Person("Steve", 27)
person3 = Person("martin", 35)


# Ordinary state
print("person.name:", person.name)

# ordinary method

person.introdcue()
person.say_age()


print("====== Ordinary & Static Properties =====")

new_message = Person.message
print("new_message:", new_message)
