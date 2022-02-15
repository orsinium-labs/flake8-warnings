from textwrap import dedent

import astroid
import pytest

from notice._extractors import DecoratorsExtractor


def p(text):
    tree = astroid.parse(dedent(text))
    print(tree.repr_tree())
    return tree


def e(node):
    return [(w.category, w.message) for w in DecoratorsExtractor().extract(node)]


@pytest.mark.parametrize('given, exp', [
    # https://github.com/tantale/deprecated
    ('deprecated(reason="use another function")', 'use another function'),
    ('deprecated.deprecated(reason="use another function")', 'use another function'),
    # https://github.com/briancurtin/deprecation
    (
        'deprecation.deprecated(details="Use the bar function instead")',
        'Use the bar function instead',
    ),
    (
        'deprecation.deprecated(deprecated_in="1.0", current_version=__version__, details="Use the bar function instead")',  # noqa
        'Use the bar function instead',
    ),
    (
        'deprecated(deprecated_in="1.0", current_version=__version__, details="Use the bar function instead")',  # noqa
        'Use the bar function instead',
    ),
    # https://github.com/mfalesni/python-deprecate
    ('deprecated(message="call to depr func")', 'call to depr func'),
    ('deprecate.deprecated(message="call to depr func")', 'call to depr func'),
    # https://github.com/multi-vac/py_deprecate
    (
        'deprecated(allowed_deprecations=[allowed_sum_caller], message="sum is no longer supported.")',  # noqa
        'sum is no longer supported.',
    ),
])
def test_extract_deprecated(given, exp):
    r = e(p(f"""
        from deprecated import deprecated

        @{given}
        def some_old_function(x, y):
            return x + y
    """).body[-1])
    assert r == [(DeprecationWarning, exp)]
