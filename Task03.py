from random import randint


FINAL = 777

current_num = 0
while current_num < FINAL:
    num = int(input("Введите целое число: "))
    if not randint(0, 12):
        raise ValueError("Случайное исключение...")
    with open("Task03.txt", "a") as f:
        f.write(str(num) + "\n")
    current_num += num
