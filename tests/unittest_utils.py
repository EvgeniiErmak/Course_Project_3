import unittest
from .utils import filter_and_sorted, get_date, mask_account_num, mask_card_num, final_mask

class TestYourFunctions(unittest.TestCase):

    def test_filter_and_sorted(self):
        data = [{'date': '2020-01-01', 'state': 'EXECUTED'},
                {'date': '2020-02-01', 'state': 'EXECUTED'},
                {'date': '2020-03-01', 'state': 'CANCELED'}]

        result = filter_and_sorted(data)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['date'], '2020-02-01')

    def test_get_date(self):
        date_str = '2020-03-25'
        result = get_date(date_str)

        self.assertEqual(result, '25.03.2020')

    def test_mask_account_num(self):
        account = 'Счет 12345'
        masked = mask_account_num(account)

        self.assertEqual(masked, 'Счет **345')

    def test_mask_card_num(self):
        card = '1234 5678 9012 3456'
        masked = mask_card_num(card)

        expected = '   1234 56** **** 3456'
        self.assertEqual(masked, expected)

    def test_final_mask(self):
        account = 'Счет 12345'
        card = '1234 5678 9012 3456'

        self.assertEqual(final_mask(account), mask_account_num(account))
        self.assertEqual(final_mask(card), mask_card_num(card))

if __name__ == '__main__':
    unittest.main()
