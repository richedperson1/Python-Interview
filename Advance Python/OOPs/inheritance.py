class Parent1:
    def __init__(self, value1):
        self.value1 = value1


class Parent2:
    def __init__(self, value2):
        self.value2 = value2


class Child(Parent2, Parent1):
    def __init__(self, value1, value2, value3):
        # Parent1.__init__(self, value1)
        # Parent2.__init__(self, value2)
        super().__init__(value2)
        self.value3 = value3


rutvik = Child(1, 2, 3)

print(rutvik.__dict__)
# print(Child.__dict__)


class Parent1:
    def __init__(self, value1):
        self.value1 = value1
        super().__init__(value1)

    def some_method(self):
        print("Parent1.some_method() called")


class Parent2:
    def __init__(self, value2):
        self.value2 = value2
        super().__init__()

    def some_method(self):
        print("Parent2.some_method() called")


class Child(Parent1, Parent2):
    def __init__(self, value1, value2, value3):
        self.value3 = value3
        super().__init__(value1)
        super().__init__(value2)

    def some_method(self):
        super().some_method()
        print("Child.some_method() called")


first = Child(1, 2, 3)
# print(first.__dict__)
