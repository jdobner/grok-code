import logging

import pytest


@pytest.fixture(scope="class")
def dummy_data(request):
    request.cls.num1 = 10
    request.cls.num2 = 20
    logging.info("Execute fixture")


@pytest.mark.usefixtures("dummy_data")
class TestCalculatorClass:
    my_val = 5

    def test_distance(self):
        logging.info("Test distance function")
        assert distance(self.num1, self.num2) == 10

    def test_sum_of_square(self):
        logging.info("Test sum of square function")
        assert sum_of_square(self.num1, self.num2) == 500

    def test_jerry(self):
        assert self.my_val == 5


# test/test_code.py::TestCalculatorClass::test_distance
# ------- live log setup -------
# INFO     root:test_code.py:59 Execute fixture
# ------- live log call -------
# INFO     root:test_code.py:65 Test distance function
# PASSED                                                                                                                                         [ 50%]
# test/test_code.py::TestCalculatorClass::test_sum_of_square
# ------- live log call -------
# INFO     root:test_code.py:69 Test sum of square function
# PASSED

# source code
def distance(num1, num2):
    return abs(num1 - num2)


def sum_of_square(num1, num2):
    return num1 ** 2 + num2 ** 2