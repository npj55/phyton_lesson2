# Date of birth of Pushkin
print('What is the year of birth of Pushkin ?')
year = str(input('input the year: '))
if year == ('1799'):
    print('What is the day of birth of Pushkin ?')
    day = input("The day is: ")
    if day == ('06.06'):
        print("Верно")
    else:
        print('Неверный день рождения')
if year != ("1799"):
    print('Не верный год рождения')
