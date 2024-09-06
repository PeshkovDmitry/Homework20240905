from Task05.UserNameError import UserNameError
from Task05.UserAgeError import UserAgeError
from Task05.UserEmailError import UserEmailError


class User:

    def __init__(self):
        self._name = ""
        self._email = ""
        self._age = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value.split()) < 2:
            raise UserNameError
        if not all([s.istitle() for s in value.split()]):
            raise UserNameError
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if not len(value.split("@")) == 2:
            raise UserEmailError
        if not value.split("@")[1].count(".") == 1:
            raise UserEmailError
        self._email = value

    @property
    def age(self):
        return self._email

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise UserAgeError
        if not value in range(0, 120):
            raise UserAgeError
        self._age = value
