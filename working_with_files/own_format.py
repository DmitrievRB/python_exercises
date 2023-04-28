#  Денис Дмитриев учит язык python
with open("students.txt","rt", encoding="utf8") as file:

      for students_data in file:
        data = students_data.upper().rstrip().split(":")

        name = data[0]
        language = data[1]
        # name, language = students_data.rstrip().split(":")# еще один вариант
        print(f"{name} учит язык  {language}!")