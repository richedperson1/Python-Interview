class Potato:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hi there! My name is {self.name}"
    
    def __call__(self,*arg,**kwarg):
        return "Hello "

class PotatoType(type):
    instance = None
    
    def __call__(cls,*arg,**kwargs):
        # print("during call : ",arg,kwargs)
        print("===========> ",cls)
        return Potato("Brown Potato")

    # def __new__(cls, name, bases, namespace,*arg, **kwargs):
    #     # print("===========> ",cls)
    #     if cls.instance:
    #         return cls.instance
    #     cls.instance = type( name, bases, namespace)
    #     return cls.instance


class Person(metaclass=PotatoType):
    def __init__(self):
        self.name = "name"
        self.age = "age"
    
    def hello(self):
        pass

# p = Person("Diwash", 24) # returns a potato object
# r = Person("Diwash", 24) # returns a potato object
p = Person() # returns a potato object
# r = Person() 
