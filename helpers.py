import datetime
import random
import string


def generating_data_day():
    """ генерация сегодняшней даты """
    data_day = str(datetime.date.today())
    return data_day


def generating_telefon_namber():
    """ генерация рандомного номера телефона """
    telefon = str(''.join(map(str, random.sample(range(10), 9))))
    namber = '+79' + telefon
    return namber


def generating_rent_time():
    """ получение рандомного числа для выбора времени аренды """
    rent_time = str(''.join(map(str, random.sample(range(1, 6), 1))))
    return rent_time


def random_metro_station():
    """ получение рандомного числа для выбора станции """
    metro_station = str(''.join(map(str, random.sample(range(1, 10), 1))))
    return metro_station


def random_name():
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(8))
    actual_name = name
    return actual_name


def last_name():
    letters = string.ascii_lowercase
    last_name = ''.join(random.choice(letters) for i in range(8))
    return last_name


def random_pass():
    """Метод генерирует рандомный пароль из букв латинского алфавита и цифр"""
    password = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    actual_password = password
    return actual_password


def random_login():
    """Метод генерирует рандомное login из букв латинского алфавита."""
    login = (f"{''.join(random.choice(string.ascii_uppercase) for i in range(1))}"
             f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}")
    actual_login = login
    return actual_login


def random_list():
    """ создание списка с рандомным логином и паролем """
    list_data = [random_login(), random_pass()]
    return list_data


