import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_Ru')
faker_en = Faker('En')
Faker.seed()


def get_value():
    data_dict = {
        1: "Hindi", 2: "English", 3: "Maths", 4: "Physics", 5: "Chemistry", 6: "Biology", 7: "Computer Science",
        8: "Commerce", 9: "Accounting", 10: "Economics", 11: "Arts", 12: "Social Studies", 13: "History", 14: "Civics"
    }
    return data_dict.get(random.randint(1, 14))


def generated_person():

    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(0, 99999),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
        subject=get_value()
    )


def generated_file():
    path = rf'C:\MyPython\QA\filetest{random.randint(0, 99)}.txt'
    with open(path, 'w+') as f:
        f.write(f'You number{random.randint(0, 99)}')
    return f.name, path


def generated_colors():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )
