import json
from typing import List


def filter_and_sorted(data: List[dict]) -> List[dict]:
    filtered = [item for item in data if item.get('state') == 'EXECUTED']
    filtered.sort(key=lambda x: x.get('date'), reverse=True)
    return filtered


def prepare_message(item: dict) -> str:
    date = get_date(item.get('date'))
    description = item.get('description', '')
    from_account = item.get('from', '')
    to_account = item.get('to', '')
    amount = item.get('operationAmount', {}).get('amount', '')
    currency = item.get('operationAmount', {}).get('currency', {}).get('name', '')

    masked_from_account = mask_card_num(from_account) if 'карта' in description else mask_account_num(from_account)
    masked_to_account = mask_account_num(to_account)

    return f'{date} {description}\n{masked_from_account} -> {masked_to_account}\n{amount} {currency}'


def get_date(date: str) -> str:
    dt = date[:10].split('-')
    return f'{dt[2]}.{dt[1]}.{dt[0]}'


def mask_account_num(msg: str) -> str:
    if msg.startswith('Счет'):
        parts = msg.split()
        if len(parts) == 2:
            return '**' + parts[1][-4:]
    return msg


# utils.py

def mask_card_num(msg: str) -> str:
    if 'карта' in msg:
        parts = msg.split()
        if len(parts) == 6:
            card_number = parts[3]  # Изменяем индекс, чтобы получить номер карты
            masked_card = ' '.join([card_number[:4], '**', '****', card_number[-4:]])
            parts[3] = masked_card  # Изменяем индекс обратно
            return ' '.join(parts)
    return msg



def final_mask(msg):
    msg = mask_card_num(msg)
    msg = mask_account_num(msg)
    return msg
