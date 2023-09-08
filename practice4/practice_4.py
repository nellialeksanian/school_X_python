from import_this import generate_race_data
def sort_racers(RACE_DATA: dict) -> dict:
    sorted_rd: dict = {}
    for value in RACE_DATA.values():
        finishplace: int = value["FinishedPlace"]
        sorted_rd[finishplace] = value
    return sorted_rd

def print_first_racer (sorted_rd: dict) -> str:
    winner: str = f"Выиграл - {sorted_rd[1]['RacerName']}!!!! Поздравляем!!!"
    print(winner + "\n" + "-" * len(winner))

def print_top_racers (sorted_rd: dict) -> str:
    print("Первые 3 места:\n")
    for k in range(1, 4):
        value: dict = sorted_rd[k]
        print(f"Гонщик на {k} месте\n" +
              f"\tИмя:{value['RacerName']} \n" +
              f"\tКоманда:{value['RacerTeam']}\n" +
              f"\tВремя:{value['FinishedTimeSeconds'] // 3600}:" +
              f"{value['FinishedTimeSeconds'] % 3600 // 60}:" +
              f"{value['FinishedTimeSeconds'] % 60} \n"
              )

if __name__ == "__main__":
    sorted: dict = sort_racers(generate_race_data(10))
    print_first_racer(sorted)
    print_top_racers(sorted)






