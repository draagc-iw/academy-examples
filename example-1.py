class Animal:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

dog = Animal("dog")
cat = Animal("cat")

dog.print_name()
cat.print_name()
