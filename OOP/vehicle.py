class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        return "The engine is now on!"
class Car(Vehicle):
    def __init__ (self,make, model, color):
        super(). __init__ (make,model)
        self.color=color
    def move(self):
        print("It is moving")
class Lorry(Vehicle):
    def __init__ (self,make,model,capacity):
        super(). __init__ (make,model)
    def unload(self):
        print("The lorry is unloading")
        