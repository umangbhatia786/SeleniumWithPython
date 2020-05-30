import unittest


class PaymentReturnsTest(unittest.TestCase):
    def test_payment_return_in_cash(self):
        print('This is payment returns test by cash')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
