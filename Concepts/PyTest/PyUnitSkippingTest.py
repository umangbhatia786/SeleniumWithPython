import unittest


class AppTest(unittest.TestCase):

    def test_search(self):
        print('This is Test Case A')

    @unittest.skipIf(1 == 1, 'Numbers are not equal')
    def test_input(self):
        print('This is Test Case B')

    @unittest.SkipTest  # Annotation to Skip a particular Test Method #Called Decorator in Python
    def test_advanced_serach(self):
        print('This is Test C')

    @unittest.skip('Skipping Because not yet ready')
    def test_twitter(self):
        print('This is Test D')

    def test_fly(self):
        print('This is Test Case E')


if __name__ == '__main__':
    unittest.main()
