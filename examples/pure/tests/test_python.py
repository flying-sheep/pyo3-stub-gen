from pure import sum, create_dict, read_dict
import pytest


def test_sum():
    assert sum([1, 2]) == 3
    assert sum((1, 2)) == 3


def test_create_dict():
    assert create_dict(3) == {0: [], 1: [0], 2: [0, 1]}


def test_read_dict():
    read_dict(
        {
            0: {
                0: 1,
            },
            1: {
                0: 2,
                1: 3,
            },
        }
    )

    with pytest.raises(TypeError) as e:
        read_dict({0: 1})  # type: ignore
    assert (
        str(e.value) == "argument 'dict': 'int' object cannot be converted to 'PyDict'"
    )