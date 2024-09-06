from Task04.ScoreLimitExceededError import ScoreLimitExceededError


class GameScore:

    def __init__(self):
        self._current_score = 0

    def add_score(self, num: int):
        if self._current_score + num > 1000:
            raise ScoreLimitExceededError
        self._current_score += num

    def subtract_score(self, num: int):
        if self._current_score - num < 0:
            raise ValueError("Счет не может быть отрицательным")
        self._current_score -= num

try:
    game_score = GameScore()
except ValueError as e:
    print(e)
except ScoreLimitExceededError as e:
    print(e)
