from Task04.ScoreLimitExceededError import ScoreLimitExceededError


class GameScore:

    def __init__(self):
        self._current_score = 0

    def add(self, score: int):
        if score > 0:
            if score > 1000:
                raise ScoreLimitExceededError
            self._current_score += score

    def sub(self, score: int):
        if self._current_score - score > 0:
            self._current_score -= score


game_score = GameScore()
game_score.add(10)
game_score.add(1110)

