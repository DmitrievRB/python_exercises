import redis
# import json

red = redis.Redis(host="redis-12918.c293.eu-central-1-1.ec2.cloud.redislabs.com",
                  port=12918,
                  password="vYHoqeZcTuFsTnX5jYzvUspXeaDxsLog")

cont = True
while cont:
    action = input("команда:\t")
    if action == "Добавить":
        name = input("Введи имя:\t")
        phone = input("Введи телефон:\t")
        red.set(name, phone)
    elif action == "Вывести":
        name = input("Введи имя:\t")
        phone = red.get(name)
        if phone:
            print(f"{name} номер телефона {phone}")

        else:
            print(f"Номер телефона {name} не найден")
    elif action == "Удалить":
        name = input("Введи имя:\t")
        phone = red.delete(name)
        if name:
            print(f"Номер телефона {name} удален")
        else:
            print(f"Номер телефона {name} не найден")
    elif action == "Отставить":
        break
