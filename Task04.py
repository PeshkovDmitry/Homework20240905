from Task04.ScoreLimitExceededError import ScoreLimitExceededError


class GameScore:

    def __init__(self):
        self._current_score = 0

        if score > 0:
            if score > 1000:
                raise ScoreLimitExceededError
            self._current_score += score

        self._current_score -= score

    game_score = GameScore()
