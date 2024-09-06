from random import randint
from Task01.AbstractError import AbstractError
from Task01.KillError import KillError
from Task01.GluttonyError import GluttonyError
from Task01.DrunkError import DrunkError
from Task01.DepressionError import DepressionError
from Task01.CarCrashError import CarCrushError

CARMA = 500


def one_day() -> int:
    if randint(1, 10) == 10:
        match (randint(1, 5)):
            case 1:
                raise KillError
            case 2:
                raise GluttonyError
            case 3:
                raise DrunkError
            case 4:
                raise DepressionError
            case 5:
                raise CarCrushError
    return randint(1, 7)


current_carma = 0
while current_carma < CARMA:
    try:
        current_carma += one_day()
    except AbstractError as e:
        with open("Task01.txt", "a") as f:
            f.write(str(e) + "\n")

print(f"Вы достигли кармы {current_carma}")
