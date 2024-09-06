from Task04.ScoreLimitExceededError import ScoreLimitExceededError


class GameScore:

    def __init__(self):
        self._current_score = 0

    def add_score(self, score: int):
        if score > 0:
            if score > 1000:
                raise ScoreLimitExceededError
            self._current_score += score

    def subtract_score(self, score: int):
        if not self._current_score - score > 0:
            raise ValueError("При снижении очков счет становится отрицательным")
        self._current_score -= score

try:
    game_score = GameScore()
    game_score.add_score(10)
    game_score.add_score(1110)
except ValueError as e:
    print(e)
except ScoreLimitExceededError as e:
    print(e)
