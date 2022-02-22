"""EX05 - tests 'list' Utility Functions from utils.py."""
__author__ = "730460523"

from utils import only_evens, sub, concat


# only_evens tests
def test_only_one_even() -> None:
    """Tests a list with only one even number."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_no_evens() -> None:
    """Tests a list with no even numbers."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_all_evens() -> None:
    """Tests a list with all even numbers."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_neg_evens() -> None:
    """Tests a list with negative even numbers."""
    xs: list[int] = [-4, 1, 4, 1]
    assert only_evens(xs) == [-4, 4]


def test_zeros() -> None:
    """Tests a list with a zero."""
    xs: list[int] = [4, 1, 4, 0]
    assert only_evens(xs) == [4, 4, 0]


# sub tests
def test_example_sub() -> None:
    """Tests general subset."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_small_sub() -> None:
    """Tests a subset with only one value."""
    xs: list[int] = [100, 35, 30, 1]
    assert sub(xs, 1, 2) == [35]


def test_empty_sub() -> None:
    """Tests a subset with an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 4) == []


def test_begin_sub() -> None:
    """Tests subset that starts at index 0."""
    xs: list[int] = [1, 2, 3, 4]
    assert sub(xs, 0, 2) == [1, 2]


def test_no_sub() -> None:
    """Tests subset with no values."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 0, 0) == []


# concat tests
def test_regular_concat() -> None:
    """Tests a concatentation of two standard lists."""
    xs1: list[int] = [6, 7, 8, 9, 10]
    xs2: list[int] = [1, 2, 3, 4, 5]
    assert concat(xs1, xs2) == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]


def test_empty_concat() -> None:
    """Tests a concatentation of two empty lists."""
    xs1: list[int] = []
    xs2: list[int] = []
    assert concat(xs1, xs2) == []


def test_one_empty_concat() -> None:
    """Tests a concatentation of one empty and one filled list."""
    xs1: list[int] = []
    xs2: list[int] = [1, 2, 3]
    assert concat(xs1, xs2) == [1, 2, 3]


def test_diff_sizes_concat() -> None:
    """Tests a concatentation of two lists of different sizes."""
    xs1: list[int] = [1, 2, 3, 4, 5]
    xs2: list[int] = [6, 7, 8]
    assert concat(xs1, xs2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_short_concat() -> None:
    """Tests a concatentation of two lists with one item."""
    xs1: list[int] = [1]
    xs2: list[int] = [2]
    assert concat(xs1, xs2) == [1, 2]
