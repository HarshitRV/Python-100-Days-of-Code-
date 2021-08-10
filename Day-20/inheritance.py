class Animal:
    def __init__(self):
        self.eyes = 2
        self.legs = 4
    def breathe(self):
        print("Inhale, Exhale.")
    def sound(self):
        print("This is how I sound")

class Dog(Animal):
    # Inheritance
    def __init__(self):
        super().__init__()

    # Function Overriding    
    def sound(self):
        super().sound()
        print("Bark")

dog = Dog()
dog.breathe()
dog.sound()