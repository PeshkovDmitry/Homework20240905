user_name = input("Введите ваше имя: ")


def show_log():
    try:
        with open("Task02.txt", "r") as f:
            for m in f.readlines():
                print(m)
    except FileNotFoundError:
        print("Файл истории сообщений не найден")


def send_message(message: str):
    with open("Task02.txt", "a") as f:
        f.write(message + "\n")


while True:
    command = input("1 - Просмотреть чат,\n2 - Написать сообщение,\n3 - Выйти\n->")
    match command:
        case "1":
            show_log()
        case "2":
            message = input("Введите сообщение -> ")
            send_message(user_name + ": " + message)
        case "3":
            break
        case "_":
            print("Команда неверна")
