from faker import Faker


fake = Faker('ru_RU')


def create_random_email():
    email = fake.free_email()
    return email


def create_random_password():
    password = fake.password(length=10)
    return password


def create_random_name():
    first_name = fake.first_name()
    return first_name