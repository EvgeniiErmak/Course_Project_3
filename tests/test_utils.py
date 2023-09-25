from .utils import filter_and_sorted, get_date, mask_account_num, mask_card_num, final_mask


def test_filter_and_sorted():
    data = [{'date': '2020-01-01', 'state': 'EXECUTED'},
            {'date': '2020-02-01', 'state': 'EXECUTED'},
            {'date': '2020-03-01', 'state': 'CANCELED'}]

    result = filter_and_sorted(data)

    assert len(result) == 2
    assert result[0]['date'] == '2020-02-01'


def test_get_date():
    date_str = '2020-03-25'
    result = get_date(date_str)

    assert result == '25.03.2020'


def test_mask_account_num():
    account = 'Счет 12345'
    masked = mask_account_num(account)

    assert masked == 'Счет **345'


def test_mask_card_num():
    card = '1234 5678 9012 3456'
    masked = mask_card_num(card)

    assert masked == '1234 56** **** 3456'


def test_final_mask():
    account = 'Счет 12345'
    card = '1234 5678 9012 3456'

    assert final_mask(account) == mask_account_num(account)
    assert final_mask(card) == mask_card_num(card)