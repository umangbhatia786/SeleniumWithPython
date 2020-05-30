import unittest


class SignupTest(unittest.TestCase):

    def test_signup_by_email(self):
        print('Test Case for signup by email')
        self.assertTrue(True)

    def test_signup_by_facebook(self):
        print('Test Case for signup by facebook')
        self.assertTrue(True)

    def test_signup_by_twitter(self):
        print('Test Case for signup by twitter')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
