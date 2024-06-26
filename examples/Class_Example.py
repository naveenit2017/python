#clss example
class myclass:
    def __init__(self,name,age) -> None:
        print(f"my name is{name} and age is {age}")
        
    print("I am from Myclass")
    def greetings(self):
        print("Hello this is naveen varma")
    def welecome(self,name):
        print(f"Thanks welcome mr {name} varma garu")

m=myclass("naveen",32)    
m.greetings()
m.welecome("naveen")

#__init__ is the initializer method that sets up the instance attributes name and age.
#self.name and self.age refer to the name and age attributes of the instance being created.

class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greetings(self):
        return f"He is my best friend is name {self.name} and age is {self.age}"
    
m=myclass("Raja",25)
print(m.greetings())
