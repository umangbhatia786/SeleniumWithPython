import unittest


class PaymentTest(unittest.TestCase):
    def test_payment_in_rupees(self):
        print('This is payment in Rupees')
        self.assertTrue(True)

    def test_payment_in_dollars(self):
        print('This is payment in Dollars')
        self.assertTrue(True)

    def test_payment_in_euros(self):
        print('This is payment in Euros')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
