print("==== Iterable Objects(Takrorlanish hususiyatiga ega Objectlar) ====")
# Iterable objects > string, dict, tuple, list, rang, map, filter


range_obj = range(3)
print("range_obj:", range_obj)
for letter in "MIT":
    print(f"The letter: {letter}")
for ele in range_obj:
    print(f'The letter: {ele}')


print("==== Dictionary ====")
# Dictionary is Json Object
person = {"name": "Nick", "age": 26, "married": True}
person_obj = dict(name="Nick", age=26, married=True)
print(f"The person: {person}")
print(f"The person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)


name2 = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 1200)
print(f"The name2: {name2}, hobby: {hobby}, balance: {balance}")

del person_obj["married"]
for key in person_obj:
    print(f"The key: {key} => value {person_obj.get(key)}")
