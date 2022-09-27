import pytest

from flake8_warnings._extractors import WarningsExtractor

from .helpers import e, p


def test_module_deprecated():
    r = e(WarningsExtractor, p("""
        import warnings
        from astroid.nodes.node_classes import (
            AsyncFor,
        )
        warnings.warn(
            "The module is deprecated and so on",
            DeprecationWarning,
        )
    """))
    assert r == [(DeprecationWarning, 'The module is deprecated and so on')]


@pytest.mark.parametrize('given, ecat, emsg', [
    ('"oh hi mark"', UserWarning, 'oh hi mark'),
    ('"oh hi mark", ImportWarning', ImportWarning, 'oh hi mark'),
    ('"oh hi mark", category=ImportWarning', ImportWarning, 'oh hi mark'),
    ('message="oh hi mark", category=ImportWarning', ImportWarning, 'oh hi mark'),
    ('category=ImportWarning, message="oh hi mark"', ImportWarning, 'oh hi mark'),

    ('"oh hi mark", garbage', Warning, 'oh hi mark'),
    ('garbage', UserWarning, 'warnings.warn(garbage)'),
    ('', UserWarning, 'warnings.warn()'),
])
def test_module_deprecated__args_parsing(given, ecat, emsg):
    r = e(WarningsExtractor, p(f"""
        import warnings
        warnings.warn({given})
    """))
    assert r == [(ecat, emsg)]
