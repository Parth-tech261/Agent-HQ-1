import sys
from pathlib import Path

# Ensure workspace root is on sys.path so tests can import `app`
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from app import add, divide


def test_add_integers_and_floats():
    assert add(1, 2) == 3
    assert add(1.5, 2.5) == 4.0


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (-1, 1, 0),
    (10**18, 1, 10**18 + 1),
])
def test_add_edge_numbers(a, b, expected):
    assert add(a, b) == expected


def test_add_strings_concatenate():
    assert add("a", "b") == "ab"


def test_add_type_error_on_incompatible_types():
    with pytest.raises(TypeError):
        add(None, 1)
    with pytest.raises(TypeError):
        add(1, None)


def test_divide_basic_cases():
    assert divide(6, 3) == 2.0
    assert divide(7, 2) == 3.5
    assert divide(5.0, 2.5) == 2.0
    assert divide(-6, 3) == -2.0


def test_divide_precision():
    assert divide(1, 3) == pytest.approx(0.3333333333, rel=1e-9)


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_divide_type_error_on_incompatible_types():
    with pytest.raises(TypeError):
        divide("a", 1)
    with pytest.raises(TypeError):
        divide(1, None)
