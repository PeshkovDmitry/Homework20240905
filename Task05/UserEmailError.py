class UserEmailError(Exception):

    def __str__(self):
        return "Неверный формат адреса электронной почты"