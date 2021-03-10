class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi ,I am {self.name}")


john = Person("john Smith")
bob = Person("Bob Smith")
john.talk()
bob.talk()
