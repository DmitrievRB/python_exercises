row_index =0
items_count =0
items_sum = 0
with open("c:/resources/shopping_list.txt",encoding="utf8") as file:
    for item_date in file:
        row_index +=1
        if item_date.count(":") < 2:
            print(f"В строке {row_index} есть ошибка")
            continue
        item,quntity,price = item_date.rstrip().split(":")
        items_count +=1
        items_sum += int(price)* int(quntity)
    print(f"В списке {items_count} позиций.Сумма {items_sum}рублей")