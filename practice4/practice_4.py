from import_this import *



# for key, value in RACE_DATA.items():
#     if key == 1:
#         RacerName = RACE_DATA


print(f"Гонщик на { RACE_DATA.get(1).get('FinishedPlace')} месте")
print(f'Имя: {RACE_DATA.get(1).get("RacerName")}')
print(f'Команда: {RACE_DATA.get(1).get("RacerTeam")}')
print(f'Время: {RACE_DATA.get(1).get("FinishedTimeSeconds")}')





