## Lists & Tuples

## Lists
# x = [10,20,30,20,50,40,60,20,20,80]

# print(x)
# print(x[0])
# print(x[1])

## List methods

## add
# x.append(100)
# x.extend([100,200,300])
# x.insert(1,100)

# # delete
# x.remove(100)
# x.pop() # last elm
# x.pop(0) # specific elm
# x.clear()

## find
# print(x.index(10))
# print(x.count(20))

# x.sort()
# x.sort(reverse=True)
# x.reverse()

# y = x.copy()
# print(y)

## stats
# print(len(x))
# print(sum(x))
# print(min(x))
# print(max(x))
# print(sum(x)/len(x))

# print(x)


## Tuples

# t = (10,20,20)
# print(t)
# # t[0] = 100 # error
# print(t[0])
# print(t.count(20))
# print(t.index(20))

# print(len(t))
# print(20 in t)


# # Single element tuple
# a = (10,)

# # Tuple without parentheses
# b = 10, 20, 30
# print(b)
# # Tuple unpacking
# x, y, z = b
# print(x, y, z)

# 3. Dictionary ({})

# -A dictionary stores data in key-value pairs.
# -Keys must be unique.
# -Values can be duplicated.
# -Mutable.
# -Maintains insertion order.

student = {
    "name": "Rahul",
    "age": 22,
    "city": "Delhi"
}

# print(student["name"])
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))
# student.update({"name":"Rahul Sharma"})
# print(student.get("name"))

# print(student)
# student.pop("name")
# student.popitem()
# print(student)

d = {
    "name": "Rahul",
    "age": 22,
    "city": "Delhi"
}

# Access
# print(d["name"])
# print(d.get("age"))

# Add
# d["course"] = "Python"

# Update
# d["age"] = 25

# Delete
# del d["city"]

# Check key
# print("name" in d)

# Loop
# for key, value in d.items():
#     print(key, value)

# Length
# print(len(d))

## 4. Set ({})
## A set stores unique elements. It is unordered, mutable, and does not allow duplicate values.
# my_set = {10, 20, 30, 40,40}
# print(my_set)
# print(my_set.add(50))
# print(my_set)
# my_set.update([50, 70])
# print(my_set)

