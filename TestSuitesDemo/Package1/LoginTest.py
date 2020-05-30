import unittest


class LoginTest(unittest.TestCase):
    def test_login_by_email(self):
        print('This is login by email')
        self.assertTrue(True)

    def test_login_by_facebook(self):
        print('This is login by facebook')
        self.assertTrue(True)

    def test_login_by_twitter(self):
        print('This is login by twitter')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
