"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import numpy as np
from inflammation.models import daily_max
from inflammation.models import daily_min
from inflammation.models import daily_mean

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max():
    data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    expected = np.array([7, 8, 9])
    actual = daily_max(data)

    np.testing.assert_array_equal(actual, expected)

def test_daily_min():
    data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    expected = np.array([1, 2, 3])
    actual = daily_min(data)

    np.testing.assert_array_equal(actual, expected)