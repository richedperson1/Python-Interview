## Design principle

- Class composition is a design principle in object-oriented programming (OOP) where a class contains objects of other classes as member variables. This allows for creating complex objects by combining simpler ones.
  </br>
  </br>

```{python}
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car starting")
        self.engine.start()

    def stop(self):
        print("Car stopping")
        self.engine.stop()


```
