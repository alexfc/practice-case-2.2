from datetime import *


def get_char(char: str) -> str:
    alphabet: dict[str: list[str]] = {
        '0': [
            '******',
            '*    *',
            '*    *',
            '*    *',
            '*    *',
            '*    *',
            '******',
        ],
        '1': [
            '     *',
            '    **',
            '   * *',
            '  *  *',
            '     *',
            '     *',
            '     *',
        ],
        '2': [
            '******',
            '     *',
            '     *',
            '******',
            '*     ',
            '*     ',
            '******',
        ],
        '3': [
            '******',
            '     *',
            '     *',
            '******',
            '     *',
            '     *',
            '******',
        ],
        '4': [
            '*    *',
            '*    *',
            '*    *',
            '******',
            '     *',
            '     *',
            '     *',
        ],
        '5': [
            '******',
            '*     ',
            '*     ',
            '******',
            '     *',
            '     *',
            '******',
        ],
        '6': [
            '******',
            '*     ',
            '*     ',
            '******',
            '*    *',
            '*    *',
            '******',
        ],
        '7': [
            '******',
            '     *',
            '     *',
            '     *',
            '     *',
            '     *',
            '     *',
        ],
        '8': [
            '******',
            '*    *',
            '*    *',
            '******',
            '*    *',
            '*    *',
            '******',
        ],
        '9': [
            '******',
            '*    *',
            '*    *',
            '******',
            '     *',
            '     *',
            '******',
        ],
        ' ': [
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
        ],
    }

    return alphabet[char]


def parse_int(value) -> int:
    try:
        return int(value)
    except:
        print('Значение должно быть целым числом')
        exit(1)


def ask_user_data(question: str, min_val: int, max_val: int) -> int:
    value = parse_int(input(question + '\n'))

    if value < min_val or value > max_val:
        print(f'Значение должно быть в пределах {min_val} от {max_val} до')
        exit(1)

    return value


def day_of_week(user_birthday: date) -> str:
    names: dict[int: str] = {
        0: 'понедельник',
        1: 'вторник',
        2: 'среда',
        3: 'четверг',
        4: 'пятница',
        5: 'суббота',
        6: 'воскресенье',
    }
    print(user_birthday.weekday())
    return names[user_birthday.weekday()]


def is_leap_year(birthday_year: int) -> bool:
    if birthday_year % 4 == 0 and (birthday_year % 100 != 0 or birthday_year % 400 == 0):
        return True

    return False


def get_user_age(user_birthday: date) -> int:
    now = datetime.today()
    age: int = now.year - user_birthday.year

    if now.day >= user_birthday.day and now.month >= user_birthday.month:
        return age

    return age - 1


def print_char(user_birthday) -> None:
    year_str = str(user_birthday.year)
    month_str = str(user_birthday.month).rjust(2, '0')
    day_str = str(user_birthday.day)

    date_str = f'{day_str} {month_str} {year_str}'
    chars: list[str] = []

    for i in range(0, len(date_str)):
        chars.append(get_char(date_str[i]))

    lines: list[str] = [''] * 11

    for i in range(0, len(chars)):
        for j in range(0, len(chars[i])):
            lines[j] += ' ' + chars[i][j]

    for line in lines:
        print(*line)


day = ask_user_data(f'Введите день вашего рождения', 1, 31)
month = ask_user_data(f'Введите месяц вашего рождения', 1, 12)
year = ask_user_data(f'Введите год вашего рождения', MINYEAR, MAXYEAR)


try:
    birthday = date(year, month, day)
    now = date.today()

    if now < birthday:
        print('Введенная дата больше текущей')
        exit(1)
except ValueError:
    print('Вы ввели недопустимую дату')
    exit(1)

print(f'+-------------------------------------------+')
print(f'Вы ввели дату: {birthday.isoformat()}')
print(f'День недели: {day_of_week(birthday)}')
print(f'Вы родились в {"високосный" if is_leap_year(birthday.year) else "не високосный"} год')
print(f'Ваш возраст: {get_user_age(birthday)}')
print_char(birthday)



