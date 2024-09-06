from Task01.AbstractError import AbstractError


class KillError(AbstractError):

    def __str__(self):
        return "Вы кого-то убили..."
