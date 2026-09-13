print("======= number ========")

# in JAVA, variable  is a name storage location
# in PYTHON, variables is names reference


count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"The count: {count}  and type {count_type}")


result1 = count.bit_count()   #method
result2 = count.numerator    #state

print(result1, result2)


print("======= string ========")
# METHODS: upper(), lower(), title(), find(), replace()
course = "AI PYTHON FULLSTACK"
result = type(course)
# print(f"The type of course: {result}")

result = course.title()
print(f"The result (1): {result}")

result = course.upper ()
print(f"The result (2): {result}")


result = course.replace("FULLSTACK", "MasterClass")
print(f"The result (3): {result}")
print(course)

# course = course.replace("FULLSTACK", "MasterClass")
# print(f"The result (3): {result}")
# print(course)


print("======= boolean ========")
# Functions => type(), input(), bool(), int(), str()
# y = input("Give your value for y: ")
# print("y:", y)


# result = y.isnumeric()
# print(f"The input value is numeric: {result}")

# TRUTHY & FALSY VALUE
# TRUTHY > TRUE, 100, -100, "MIT"
# FALSY > FALSE, 0, "", None

test_falsy = "" or False or None or 0
print("THE FALSY:", bool(test_falsy))


test_truthy = "MIT"
print("THE TRUTHY:", bool(test_truthy))
