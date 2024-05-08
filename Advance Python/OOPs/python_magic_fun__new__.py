class aa: 
    emp = 0
    first = []
    # def __new__(cls):
    #     cls.emp+=1
    #     if cls.emp>2: 
    #         print("Connected") 
    #         return super().__new__(cls)
    #     else:
    #         print("transfer get start")
    #         return cls
    
    def calling(self):
        self.first.append(2)
        return self.first
  
    def __init__(self): 
        print("Init is called") 
        self.first1 = 5



a1 = aa()
a2 = aa()
a3 = aa()
a4 = aa()
# print(a1.__dir__,a2,a3)
print(a1.__sizeof__())