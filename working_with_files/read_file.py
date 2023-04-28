guest_count = 0
with open('test.txt','rt') as file:

    for line in file:
        print(line)
        guest_count += 1

print(f"количество гостей : {guest_count}")