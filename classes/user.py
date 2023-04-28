class User:

    """ Модель пользователя"""

    def __init__(self, name, email, created_at, is_email_verified, purchases):
        self.name = name
        self.email = email
        self.created_at = created_at
        self.is_email_verified = is_email_verified
        self.purchases = purchases
        print("Пользователь создан")

    def description_user(self):
        description = (self.name + self.email + str(self.is_email_verified) + str(self.created_at) + str(self.is_email_verified) + str(self.purchases))
        print(description)



class Product:
    def __init__(self,name,category,is_available,quantity_in_stock,vendor,manager):
        self.name = name
        self.category = category
        self.is_available = is_available
        self.quantity_in_stock = quantity_in_stock
        self.vendor = vendor
        self.manager = manager
        """Класс продуктов создан"""
    print("Продукты созданы")

    def is_product_available(self):
          return True if self.quantity_in_stock > 0 else False
          # print(pris_product_available)


"""Заведение пользователей"""
user_peter = User ('Peter',"peterrobertson@mail.com","2019-05-05",True,["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"])
user_julia = User("Julia Donaldson","juliadonaldson@mail.com", "2019-06-13", True, ["Egg", "Spam", "Magic Brush"],)
"""Завеление продуктов"""
product_egg = Product("Egg", "food", False,  2, "Dark Knight LTD",  "William The Conqueror",)
user_peter.description_user()
print(product_egg.is_product_available())
