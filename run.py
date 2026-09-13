# Dunder __builtins__, __init__


message = ("PYTHON: Everything is object!")
print(message)

result = type(message)
print("result:", result)

'''
In Python, there are bultin tools:
(1). TYPES => int, float, str, list, dict
(2). FUNCTION => print(), len(), input(), type()
(3). CONSTANTS => TRUE, FALSE, NONE
'''


print(dir(__builtins__))
# Functions => type(), input(), bool(), int(), str()

y = input("Give your value for y: ")
