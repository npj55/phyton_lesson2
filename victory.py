# Викторина
answers = 0
value = 5
wrong = 0
while True:
#1985
    year = input('Какой год рождения Александра Овечкина ?')
    if year == '1985':
        print('Верно')
        answers += 1
    else:
        print('Не верно')
        wrong += 1
#1963
    year = input('Какой год рождения Брэда Питта ?')
    if year == '1963':
        print('Верно')
        answers += 1
    else:
        print('Не верно')
        wrong +=1
#1975
    year = input('Какой год рождения Анджелины Джоли ?')
    if year ==  '1975':
        print('Верно')
        answers += 1
    else:
        print('Не верно')
        wrong += 1
#1973
    year = input('Какой год рождения Леонардо Ди Каприо ?')
    if year ==  '1973':
        print('Верно')
        answers += 1
    else:
        print('Не верно')
        wrong += 1
#1981
    year = input('Какой год рождения Джессики Альбы ?')
    if year ==  '1981':
        print('Верно')
        answers += 1
    else:
        print('Не верно')
        wrong += 1
    print(answers,' верных ответов ', value)
    print(wrong,' не верные ответы')
    print(answers * 100 / value)
    print(wrong * 100 / value)
    restart = input('Желаете начать сначала ?')
    while restart:
        restart = "Да"
        print(year)
    else:
     break