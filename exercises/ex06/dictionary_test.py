"""EX06 - Tests Dictonary Functions from dictionary.py."""
__author__ = "730460523"

from dictionary import invert, count, favorite_color
import pytest


# Invert tests:
def test_invert_chars() -> None:
    """Tests a dictionary with characters as keys and values."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words() -> None:
    """Tests a dictionary with words as keys and values."""
    b: dict[str, str] = {'apple': 'cat'}
    assert invert(b) == {'cat': 'apple'}


"""Tests the KeyError."""
with pytest.raises(KeyError):
    c = {'katie': 'chai', 'latte': 'chai'}
    invert(c)


# Count tests:
def test_count_ints() -> None:
    """Tests a list with integers as values."""
    d: list[str] = ["hello", "hi", "hey", "hi"]
    count(d)
    assert count(d) == {'hello': 1, 'hi': 2, 'hey': 1}


def test_count_empty() -> None:
    """Tests an empty list."""
    e: list[str] = []
    count(e)
    assert count(e) == {}


def test_count_same() -> None:
    """Tests a list with all values being the same."""
    f: list[str] = ["yo", "yo", "yo", "yo"]
    count(f)
    assert count(f) == {'yo': 4}


def test_count_two() -> None:
    """Tests a list with two, different values."""
    g: list[str] = ["yo", "whatsup"]
    count(g)
    assert count(g) == {'yo': 1, 'whatsup': 1}


# Favorite Color tests:
def test_favorite_color_blue() -> None:
    """Tests a dictionary with an single favorite color."""
    h: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(h) == "blue"


def test_favorite_color_multiple() -> None:
    """Tests a dictionary with two favorite colors."""
    i: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Katie": "yellow"}
    assert favorite_color(i) == "yellow"


def test_favorite_color_none() -> None:
    """Tests a dictionary with no favorite color."""
    j: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green", "Katie": "purple"}
    assert favorite_color(j) == ""
