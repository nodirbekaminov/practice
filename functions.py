'''FUNCTIONS
(1) DEFINE & CALL
(2) PARAMETER & ARGUMENT
(3) KEYWORD & DEFAULT ARGUMENTS
(4) SCOPE
'''

print("==== DEFINE(PARAMETER) & CALL(ARGUMENT) ====")
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


print("==== KEYWORD & DEFAULT ARGUMENTS ====")
# DEFINE


def give_greet(name, age=25):
    print("Give greet is executed")
    return f"Hi {name}, you are {age} years old!"

# Call


result3 = give_greet(name="Nick", age=26)
print("result3:", result3)


result4 = give_greet("John")
print("result4:", result4)


print("==== SCOPE ====")

b = 100  # 3 => functionsdan tashqaridagi valueni oladi!

# DEFINE


def calculate(a):  # 2 => Parametr qismidan izlaydi
    c = a * b  # 1 => Ickaridan izlaydi
    print(f"The c value is {c}")


calculate(5)
