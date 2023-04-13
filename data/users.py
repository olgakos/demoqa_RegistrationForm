from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    month_of_birth: str
    year_of_birth: str
    day_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str