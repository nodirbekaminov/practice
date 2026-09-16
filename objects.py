'''     OBJECTS
    (1). What is Object
    (2). Iterable objects & RANGE
    (3). DICTIONARY
    (3). Error Handling System
'''

import array  # package/module
import math  # package
from math import ceil, asin
print("==== What is Object ====")

# An Object has state and method properties!
# Everything is object in Python!

print(type('Hello World!'))
print(type(12121))
print(type(True))
print(type(array))
print(type(math))

# PARADIGM > Functional Programming & OOP
# OOP 4 Concepts > Abstraction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # CALL
print("result1:", result1)


result2 = ceil(98.7)  # CALL
print("result2:", result2)


print("==== Error Handling Sytem ====")
car_dict = dict(name="Toyota", year=2026, electric=True)
try:
    print("Passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed found:", err)
else:
    print("Executed successfully without errors")

finally:
    print("Final closing logic!")
