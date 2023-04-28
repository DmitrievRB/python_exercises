class Article():
    def __init__(self,content):
        self.content = content
class Article_Extented(Article):
    def count_simbol(self,):
        return len(self.content)
    def count_word(self):
        word = self.content.split()
        return len(word)


article = Article_Extented(
    """Ваш баланс составляет $ -567.072.565,13.
    Номер заблокирован.
    Вас ожидает 26 рабства на урановых рудниках"
    Одна СМСка. Чертов роуминг на Сириусе." (с) Юрий Ермаков - Баланс    """)
print(article.count_simbol())
print(article.count_word())

