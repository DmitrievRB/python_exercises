class User:
    def __init__(self,firstname,lastname,town,balance):
        self.firstname = firstname
        self.lastname = lastname
        self.town = town
        self.balance = balance
    def print_user(self):
        return f"{self.firstname}. {self.lastname}. {self.town}. {self.balance} руб."
    user_1 = User("Иван","Петров","Москва",50)
    print(print_user())
