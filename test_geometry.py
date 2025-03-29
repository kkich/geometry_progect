import pytest
from geometry import get_area

def test_area():
    assert get_area("rectangle", width=5, height=10) == 50
    assert get_area("square", side=4) == 16
