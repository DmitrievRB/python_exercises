from cat import Cats


class Breed(Cats):
    def __init__(self, name, gender, age, breed):
        Cats.__init__(self, name, gender, age)
        self.breed = breed

    def description_breed(self):
        desc_breed = (self.name + self.gender + self.age + self.breed)
        print(desc_breed)


cat1 = Breed("Сэм", "мальчик", "2года", "сибирская кошка")
cat2 = Breed("Барон", "мальчик", "2года", "сиамский кот")
print(cat1.description_cats())
print(cat2.description_breed())
