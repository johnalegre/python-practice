#classes and obects practice
#How to define classes in python

class vehicle: #base class - defines blueprint for all vehicles
    def __init__(self, bodystyle): #init is the constructor method - runs when creating a new object
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed #self refers to the current object ie car1 or mc1 etc

class car(vehicle):      # inherits from vehicle
    def __init__(self, enginetype, color, model):
        super().__init__("Car") # super calls parent class constructor
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype # attributes added
        self.color = color
        self.model = model

    def drive(self, speed):
        super().drive(speed)
        print(f"driving my {self.color} {self.model} {self.engine}, {self.speed} mph")

class Motorcycle(vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar): # additional logic added
            self.wheels = 3
        else:
            self.wheels = 2

        self.doors = 0
        self.enginetype = enginetype

# creation of objects
car1 = car("gas", "gray", "Lexus IS300")
car2 = car("electric", "blue","Honda Civic")
mc1 = Motorcycle("gas", True)

# print(mc1.wheels)
# print(car1.engine)
# print(car2.doors)
# car1.drive(30)
# car2.drive(40)

print(car1.color)
print(car2.model)
car1.drive(90)


# Notes;
ClassesDefine reusable components (e.g., cloud resources, AI models, automation tasks)InheritanceExtend base functionality (e.g., base cloud resource → specialized VM or container)EncapsulationKeep logic clean and modular (e.g., API wrappers, SDKs)PolymorphismHandle different types of resources or models with shared interfaces