# main.py
import json
from datetime import datetime
from utils import filter_and_sorted, prepare_message, final_mask

# Чтение данных из operations.json
with open('operations.json', 'r', encoding='utf-8') as file:
    operations = json.load(file)

# Фильтрация и сортировка операций
sorted_operations = filter_and_sorted(operations)

# Вывод последних 5 операций
for operation in sorted_operations[:5]:
    message = prepare_message(operation)
    masked_message = final_mask(message)
    print(masked_message + '\n')
