
"""
Singletone design pattern using new static method which will act as the the static constructor.

"""
class singletone:
    _instance = None
    
    def __new__(cls,first,second):
        if cls._instance:
            return cls._instance
        
        cls._instance = super().__new__(cls)
        
        return cls._instance
    
    def __init__(self,first,second):
        self.first = first
        self.second= second
        
    
    def connection(self):
        flag = hasattr(singletone,"mysql")
        if hasattr(singletone,'mysql'):
            print("previously connected")
            return self.mysql
        print("connecting first time")
        singletone.mysql = "connected"
        return self.mysql

obj1 = singletone(1,2)

obj2 = singletone(1,3)

obj1.connection()
obj2.connection()
# print(obj1 is obj2)


