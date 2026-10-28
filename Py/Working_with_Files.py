
# a = open("new.py","r")
# print(a.read())
# a.close()

# with open("new.py","r") as a:
#     print(a.read())


# with open("new.py","w") as a:
#     a.write(input("type :"))


# with open("new.py","a") as a:
#     a.write("\n" + input("type :"))




# fn = "demo_text.txt"
# fn = "naman.html"
fn = "demo_text.txt"

# with open(fn,"r") as f:
#     x = f.read()
#     print(x)

# fn = "demo_text.txt"

# with open(fn,"r") as f:
#     x = f.readlines()
#     print(x)

# fn = "demo_text.txt"

# with open(fn,"w") as f:
#     f.write("Hello, World!")
    

# with open("abcd.txt","w") as f:
#     f.write("Hello, World!")


# fn = "demo_text.txt"

# with open(fn,"a") as f:
#     f.write("Hello, World!")
    

# import os

# print(os.path.exists(fn))

# if os.path.exists("data.txt"):
#     print("File exists")
# else:
#     print("File does not exist")


import csv

# with open("Sales_Data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# data = [
#     ["Name", "Age", "City"],
#     ["Varun", 25, "Delhi"],
#     ["Rahul", 22, "Mumbai"]
# ]

# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

    
import os

# os.rename("data.csv", "new_data.csv")
os.remove("new_data.csv")
