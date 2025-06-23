from helpers import create_random_email, create_random_password, create_random_name

class DataUser:
    DATA_USER = {
        "email": "Simba_Li@yandex.ru",
        "password": "712345",
        "name": "Sim"
    }

    DATA_USER_NO_EMAIL = {
        "email": "",
        "password": create_random_password(),
        "name": create_random_name()
    }

    DATA_USER_NO_PASSWORD = {
        "email": create_random_email(),
        "password": "",
        "name": create_random_name()
    }

    DATA_USER_NO_NAME = {
        "email": create_random_email(),
        "password": create_random_password(),
        "name": ""
    }

class DataUserAuthInvalid:
    INVALID_CREDENTIALS = [
        ("SimbaS@yandex.ru", "712345"),  # неверный email
        ("Simba_Li@yandex.ru", "777777"),  # неверный пароль
        ("", "712345"),  # пустой email
        ("Simba_Leon@yandex.ru", ""),  # пустой пароль
        ]



class DataIngredient:
    burger = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa74']


    invalid_hash_ingredient = ['61c0c5a71d1f82001bdaaa6g', '61c0c5a71d1f82001bdaaa7a','61c0c5a71d1f82001bdaaa75']

