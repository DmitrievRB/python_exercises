class Cats:
    def __init__(self, name, gender, age):
        self.age = age
        self.gender = gender
        self.name = name

    def description_cats(self):
        description = (self.name + self.gender + self.age)
        print(description)
