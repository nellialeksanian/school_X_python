from import_this import generate_race_data


def to_sort_spisok(race_data: dict) -> dict:
    new_sorted_dict: dict = {}
    for i in race_data.values():
        new_sorted_place: int = i['FinishedPlace']
        new_sorted_dict[new_sorted_place] = i
    return new_sorted_dict


def first_place(new_sorted_dict: dict) -> str:
    first_place_name: str = f'Выиграл - {new_sorted_dict[1]["RacerName"]}!!!! Поздравляем!!!'
    print(first_place_name + '\n' + '-'*len(first_place_name))


def all_victory_places(new_sorted_dict: dict) -> str:
    print('Первые 3 места:\n')
    for k in range(1, 4):
        print(f'Гонщик на {k} месте\n' +
              '\t' + f'Имя: {new_sorted_dict[k]["RacerName"]}\n' +
              '\t' + f'Команда: {new_sorted_dict[k]["RacerTeam"]}\n' +
              '\t' + f'Время: {new_sorted_dict[k]["FinishedTimeSeconds"] // 3600}:' +
              f'{new_sorted_dict[k]["FinishedTimeSeconds"] % 3600 // 60}:' +
              f'{new_sorted_dict[k]["FinishedTimeSeconds"] % 60}')


if __name__ == '__main__':
    final_dict: dict = to_sort_spisok(generate_race_data(10))
    first_place(final_dict)
    all_victory_places(final_dict)
