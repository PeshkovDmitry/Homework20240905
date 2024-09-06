class ScoreLimitExceededError(Exception):

    def __str__(self):
        return "Количество очков превысило 1000"
