from import_this import generate_race_data


def sort_racers(race_data: dict) -> dict:
    sorted_rd: dict = {}
    for value in race_data.values():
        finish_place: int = value["FinishedPlace"]
        sorted_rd[finish_place] = value
    return sorted_rd


def print_first_racer(sorted_rd: dict):
    winner: str = f"Выиграл - {sorted_rd[1]['RacerName']}!!!! Поздравляем!!!"
    print(winner + "\n" + "-" * len(winner))


def print_top_racers(sorted_rd: dict):
    print("Первые 3 места:\n")
    for k in range(1, 4):
        value: dict = sorted_rd[k]
        print(f"Гонщик на {k} месте\n" +
              f"\tИмя:{value['RacerName']} \n" +
              f"\tКоманда:{value['RacerTeam']}\n" +
              f"\tВремя:{value['FinishedTimeSeconds'] // 3600}:" +
              f"{value['FinishedTimeSeconds'] % 3600 // 60}:" +
              f"{value['FinishedTimeSeconds'] % 60} (H:M:S) \n"
              )


if __name__ == "__main__":
    sorted_dict: dict = sort_racers(generate_race_data(10))
    print_first_racer(sorted_dict)
    print_top_racers(sorted_dict)
