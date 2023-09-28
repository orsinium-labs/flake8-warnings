from textwrap import dedent

import astroid
import pytest

from flake8_warnings._finder import WarningFinder


def p(text):
    tree = astroid.parse(dedent(text))
    print(tree.repr_tree())
    return tree


def e(node):
    return [(w.category, w.message) for w in WarningFinder(node).find()]


@pytest.mark.parametrize('given, etype, emsg', [
    ('import tests.samples.warnings_module', DeprecationWarning, 'mod warn'),
    ('from tests.samples.warnings_module import fun', DeprecationWarning, 'mod warn'),
    ('from tests.samples.warnings_function import func', DeprecationWarning, 'func warn'),
])
def test_finder__import(given, etype, emsg):
    r = e(p(given))
    assert r == [(etype, emsg)]
