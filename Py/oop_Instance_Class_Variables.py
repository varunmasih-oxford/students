# class student:
    
#     session_year = 2026 # class variable

#     def __init__(self,name,roll):
#         self.name = name # instance variable
#         self.roll = roll

#     def show(self):
#         print("Student Name:", self.name)


# create objects of the student class
# s1 = student("Alice", 1)
# s2 = student("Bob", 2)


# instance variable
# print(s1.name)
# print(s2.name)

# class variable
# print(s1.session_year)
# print(s2.session_year)

# method
# s1.show()
# s2.show()

# Inheritance

# class main():

#     def fun_x(self):
#         print("Function X")

# class sub(main):

#     def fun_y(self):
#         print("Function Y")


# m = main()
# s = sub()

# s.fun_x()


# Polymorphism

# class Dog:
#     def sound(self):
#         print("Dog barks")

# class Cat:
#     def sound(self):
#         print("Cat meows")

# d = Dog()
# c = Cat()

# d.sound()
# c.sound()

# Encapsulation

class Bank:
    def __init__(self):
        self.__balance = 5000   # private variable
        

    def shw_balance(self):
        print(self.__balance)

b1 = Bank()
# b1.show_balance()
print(b1.__balance)  # This will raise an AttributeError because __balance is private