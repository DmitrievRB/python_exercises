print('Добро пожаловать в игру Лабиринт')
print('Чтобы выбрать куда направится,введите одно слово из заключенных в кавычки')
room = 1
while room > 0:
    if room == 1:
        print('Вы находитесь в пещере на развилке. Вы можете пойти «налево», «направо» или «прямо».')
        direction = input()
        while direction != 'налево' and direction != 'прямо' and direction != 'направо':
            direction = input()
        if direction == 'налево':
            print('Вы пошли налево.')
            room = 2
        elif direction == 'прямо':
            print('Вы увидели пирата,который прятал своё сокровище.')
            room = -1
        elif direction == 'направо':
            print('Вы зашли в тёмную комнату,через некоторое время вы упали к тоннелям')
            room = -1
    elif room == 2:
        print('Вы выберете «левый» или «правый»? Или повернёте «назад»?')
        direction = input()
        while direction != 'левый' and direction != 'правый' and direction != 'назад':
            direction = input()
        if direction == 'левый':
            print('Вы вернулись в тёмную комнату')
            room = -1
        elif direction == 'правый':
            print('Вы смело вошли в правый тоннель. Но за ней вас поджидал пират,который вас убил')
            room = -2
        elif direction == 'назад':
            print('Вы отправились к начальной развилке.')
            room = 1
            print('Добро пожаловать в игру Лабиринт')
            print('Чтобы выбрать куда направится,введите одно слово из заключенных в кавычки')
            room = 1
            while room > 0:
                if room == 1:
                    print('Вы находитесь в пещере на развилке. Вы можете пойти «налево», «направо» или «прямо».')
                    direction = input()
                    while direction != 'налево' and direction != 'прямо' and direction != 'направо':
                        direction = input()
                    if direction == 'налево':
                        print('Вы пошли налево.')
                        room = 2
                    elif direction == 'прямо':
                        print('Вы увидели пирата,который прятал своё сокровище.')
                        room = -1
                    elif direction == 'направо':
                        print('Вы зашли в тёмную комнату,через некоторое время вы упали к тоннелям')
                        room = -1
                elif room == 2:
                    print('Вы выберете «левый» или «правый»? Или повернёте «назад»?')
                    direction = input()
                    while direction != 'левый' and direction != 'правый' and direction != 'назад':
                        direction = input()
                    if direction == 'левый':
                        print('Вы вернулись в тёмную комнату')
                        room = -1
                    elif direction == 'правый':
                        print('Вы смело вошли в правый тоннель. Но за ней вас поджидал пират,который вас убил')
                        room = -2
                    elif direction == 'назад':
                        print('Вы отправились к начальной развилке.')
                        room = 1