alpha =  'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
num_input =int(input('Введите ключ от 1 до 32'))
while num_input == 0 or num_input ==33 or num_input ==-33:
    print("Не трать мое время введи допустимые цифры")
    num_input = int(input('Введите ключ от 1 до 32'))
number = num_input
print("Молодец, сейчас замутим")
summary =''
def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char)+number)% len(alpha)]

    elif char in alphUp:
        return alphUp[(alphUp.index(char)+number) % len(alphUp)]
    else:
        return char

with open("../doc/karenina.txt", "rt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("../doc/karenina.txt","w",encoding="utf8") as myFile:
    myFile.write(summary)
