import pytest
from geometry import get_rectangle_area, get_square_area

def test_rectangle_area():
    assert get_rectangle_area(5, 10) == 50

def test_square_area():
    assert get_square_area(4) == 16
