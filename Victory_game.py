def fp_2():
    n = input('Как тебя зовут?')
    print('Привет', n)
    a = str(input('Ты готов?'))
    if str(a) == "Да":
        fp()
    else:
        print('Пока')

def fp():
    import random
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                            'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                            'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                            'Сергей Павлович Королев': '12.01.1907'}

    rounds = int(input('Сколько раз вы хотите играть?'))
    if rounds > 10:
        print('Слишком много')
        exit()

    for i in range (rounds):
        name,date = random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input(f'Когда родился {name}?')
        if answer == date:
            print('Верно')
        else:
            print('Неверно')
    print('Пока')

    if rounds > 10:
        print('слишком много')

fp_2()