from app import add


def test_add():
    assert add(4, 3) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
