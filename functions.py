'''FUNCTIONS
(1) DEFINE & CALL
(2) PARAMETER & ARGUMENT
(3) KEYWORD & DEFAULT ARGUMENTS
(4) SCOPE
'''

print("==== DEFINE & CALL ====")
# build in functions => print(), type()
# Function => reusable block of code
# Instead of block {} in JAVA, Python uses indentation


# DEFINE => build(parameter)
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print(f"Greeting is executed")
    return f"Hi {b}"


# CALL => execute(argument)
result1 = greet("Nick")
print("result1", result1)


result2 = greeting("John")
print("result2", result2)
