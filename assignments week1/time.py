def time_converter(seconds: int):
    minutes = seconds % 3600 // 60
    hours = seconds // 3600
    print(f'{hours} час(а/ов) и {minutes} минут(а/ы)')


if __name__ == "__main__":
    seconds_input = int(input("Введите количество секунд"))
    time_converter(seconds_input)
