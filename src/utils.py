# Фильтрует и сортирует список по дате 
def filter_and_sorted(all_information: list):
    # Фильтрует список по значению state
    item = [item for item in all_information if item.get("state") == "EXECUTED"]

    # Сортирует отсортированный список по дате в обратном порядке
    item.sort(key=lambda x: x.get("date"), reverse=True)

    # Возвращает первые 5 элементов
    return item[0:5]


# Преобразует дату в нужный формат
def get_date(date: str):
    dt = date[0:10].split(sep="-")
    return dt[2] + "." + dt[1] + "." + dt[0]


# Маскирует номер счета, оставляя видимыми первые 4 цифры
def mask_account_num(msg: str):
    return "Счет **" + msg[7:11]


# Маскирует номер карты, оставляя видимыми первые 4 и последние 4 цифры
def mask_card_num(msg: str):
    operation_word = ""
    operation_numb = ""
    for word in msg:
        if not word.isnumeric():
            operation_word += word
        else:
            operation_numb += word
    operation_numb = operation_numb[0:4] + " " + operation_numb[4:6] + "** ****" + " " + operation_numb[12:]
    return operation_word + operation_numb


# В зависимости от первого символа вызывает маскирование счета или карты
def final_mask(msg):
    if msg[0] == "С":
        return mask_account_num(msg)
    else:
        return mask_card_num(msg)