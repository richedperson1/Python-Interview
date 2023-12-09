from abc import ABC,abstractmethod


class Parent(ABC):
    def main_call(self):
        return "This is main function"
    
    @abstractmethod
    def sequrity(self):
        pass
    
    
class child(Parent):
    def child_main(self):
        return "Not found"
    
    def sequrity(self):
        first = "hello"
        second = "not found"
        return first+ second
    
    
obj = child()
pObj = Parent()




# from abc import ABC, abstractmethod

# class Parent(ABC):
#     @classmethod
#     def main_call(cls):
#         return "This is main function"
    
#     @abstractmethod
#     def security(self):
#         pass

# # Creating an instance of the Parent class
# pObj = Parent()

# # Accessing the main_call() method through the instance of the Parent class
# result = pObj.main_call()
# print(result)  # Output: This is main function
