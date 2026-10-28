# print("adsf")

# name = "vishal"
# age = 20

# def show_details():
#    print("hello")



class abc():

    # Attributes
    # name = "vishal"
    # age = 20

    # constructor function
    
    def __init__(self,n,a):
        self.name = n
        self.age = a


        
    # Methods
    def show_details(self):
        print("hello my name is", self.name," and i am",self.age)

#object1    
x = abc("vishal",20)
print(x.name)
print(x.age)
x.show_details()


#object2
y = abc("Avishi",20)
y.show_details()
