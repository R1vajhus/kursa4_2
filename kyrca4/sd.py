import datetime

current_year = datetime.datetime.now().year  # Получаем текущий год

# Создаем список с годами, используя генератор списков
years_list = [year for year in range(1900, current_year + 1)]

print(years_list)