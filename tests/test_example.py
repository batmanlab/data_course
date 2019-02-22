import numpy as np
import pytest


@pytest.fixture
def data():
    np.random.seed(111)
    return np.random.normal(size=10)


def test_ex0():
    assert(1+2 == 3)


def test_ex1(data):
    data2 = data.copy()
    np.testing.assert_array_equal(data, data2)


def test_ex2(data):
    data2 = data.copy()
    data2[5] += 10
    np.testing.assert_array_equal(data, data2)


def test_ex3():
    with pytest.raises(AssertionError):
        assert(1 == 2)
