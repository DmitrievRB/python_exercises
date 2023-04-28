user_language =input("Какой язык Вы учите?")
user_time = input("Как давно?")
user_instruction =input("Где?")
with open('c:/resources/answers.txt','wt') as file:
    file.write(f"{user_language}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_instruction}\n")
print(f"Все удачно записалось")

with open('c:/resources/answers.txt','rt') as file:

    for line in file:
        print(line)


