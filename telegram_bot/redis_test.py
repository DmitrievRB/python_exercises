import redis
import  json

red = redis.Redis(host="redis-12918.c293.eu-central-1-1.ec2.cloud.redislabs.com",
                  port= 12918,
                  password="vYHoqeZcTuFsTnX5jYzvUspXeaDxsLog")
# red.set("var1","value1")

dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
red.delete("dict1","var1","converted_dict")
print(type(converted_dict)) # убеждаемся, что получили действительно словарь
print(converted_dict) # ну и выводим его содержание
print(red.get("var1"))
print(red.get("dict1"))
