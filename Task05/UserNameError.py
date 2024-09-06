class UserNameError(Exception):

    def __str__(self):
        return "Неверный формат имени"