from flake8_warnings._extractors._base import CODES, NAMES


def test_codes():
    assert len(CODES) == len(set(CODES.values()))
    last_code = max(CODES.values())
    assert set(CODES.values()) == set(range(1, last_code + 1))


def test_names():
    assert NAMES['UserWarning'] is UserWarning
