class UserAgeError(Exception):

    def __str__(self):
        return "Неверный формат возраста"