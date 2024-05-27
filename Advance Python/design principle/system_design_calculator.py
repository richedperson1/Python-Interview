from abc import ABC,abstractmethod


class operant_blueprint(ABC):
    @abstractmethod
    def operation(self,first,second):
        pass
    
    
class subtraction(operant_blueprint):
    def operation(self,first,second):
        return first - second
    
    
    
class addition(operant_blueprint):
    def operation(self,first,second):
        return first + second
    
    
    
class division(operant_blueprint):
    def operation(self,first,second):
        return first / second
    
class multiplication(operant_blueprint):
    def operation(self,first,second):
        return first * second
    
    
class calculator:
    def operation(self,first,second,operant):
        return operant.operation(first,second)


div_obj = division()

cal_obj = calculator()
first,second = 5,4


print(cal_obj.operation(first,second,div_obj))