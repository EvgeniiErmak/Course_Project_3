import json
import os.path
from typing import Union


def filter_and_sorted(data: list) -> list:
    item = [item for item in data if item.get('state') == 'EXECUTED']
    item.sort(key=lambda x: x.get('date'), reverse=True)


# a = os.path.join('data', 'operations.json')
# with open(a) as file:
#     data = json.load(file)
#
# print(filter_and_sorted(data))


def prepare_message(item: dict) -> str:
    # data = get_date(item.get('date'))
    pass

def get_date(date: str) -> str:
    dt = date[0:10].split(sep='-')
    return dt[2] + '.' + dt[1] + '.' + dt[0]



def mask_account_num(msg: str) -> str:
    pass

def mask_card_num(msg: str) -> str:
    pass

def final_mask(msg):
    pass