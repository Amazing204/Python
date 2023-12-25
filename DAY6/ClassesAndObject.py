class Person:

    def __init__(self, name, age):
        # Initialize the attributes
        self.name = name
        self.age = age

    def introduce(self):
        # Print an introduction message
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")


obj1 = Person("tarun",23)
obj1.introduce()