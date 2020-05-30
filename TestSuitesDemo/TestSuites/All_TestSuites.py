import unittest

from TestSuitesDemo.Package1.LoginTest import LoginTest
from TestSuitesDemo.Package1.SignupTest import SignupTest
from TestSuitesDemo.Package2.PaymentReturnsTest import PaymentReturnsTest
from TestSuitesDemo.Package2.PaymentTest import PaymentTest

# getting all test cases from classes
tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc_3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc_4 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

# creating TestSuites

sanity_test_suite = unittest.TestSuite([tc_1, tc_2])  # sanity test suite
functional_test_suite = unittest.TestSuite([tc_3, tc_4])
master_test_suite = unittest.TestSuite([tc_1, tc_2, tc_3, tc_4])

unittest.TextTestRunner(verbosity=2).run(master_test_suite)
