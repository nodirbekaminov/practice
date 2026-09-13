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
