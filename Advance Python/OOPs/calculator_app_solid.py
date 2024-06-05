from abc import ABC, abstractmethod
from typing import Dict, Callable
from math import tan
# Operation Interface
class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

# Concrete Operations
class Addition(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

class spliting(Operation):
    def execute(self,a:str,splitAt:str):
            return a.split(splitAt)

class tanh(Operation):
    def execute(self,a):
        return tan(a)
# Calculator Class
class Calculator:
    def __init__(self):
        self._operations: Dict[str, Operation] = {}

    def register_operation(self, operator: str, operation: Operation):
        self._operations[operator] = operation

    def calculate(self, operator: str,*arg) -> float:
    
        if operator not in self._operations:
            raise ValueError(f"Operation '{operator}' not supported")
        return self._operations[operator].execute(*arg)

# Application setup
def main():
    calculator = Calculator()
    calculator.register_operation('+', Addition())
    calculator.register_operation('tanh', tanh())
    calculator.register_operation('split', spliting())
    

    try:
        print(f"3 + 5 = {calculator.calculate('+', 3, 5)}")
        print(f" {calculator.calculate('tanh', 10)}")
        print(calculator.calculate('split', "rutvik:jaiswal",":"))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()