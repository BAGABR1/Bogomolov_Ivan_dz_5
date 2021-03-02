def gen_tuple():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена', 'Александр', 'Инокентий', 'Игорь'
        ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    if len(tutors) > len(klasses):
        for i in range(len(klasses), len(tutors)):
            klasses.append(None)
    a = ((tutors[i], klasses[i]) for i in range(len(tutors)))
    print(*a)
    print(type(a))


gen_tuple()
