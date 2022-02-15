from textwrap import dedent

import astroid
import pytest

from notice._finder import WarningFinder


def p(text):
    tree = astroid.parse(dedent(text))
    print(tree.repr_tree())
    return tree


def e(node):
    return [(w.category, w.message) for w in WarningFinder(node).find()]


ASTROID_WARNING = "The 'astroid.node_classes' module is deprecated and will be replaced by 'astroid.nodes' in astroid 3.0.0"  # noqa


@pytest.mark.parametrize("given, etype, emsg", [
    ("import astroid.node_classes", DeprecationWarning, ASTROID_WARNING),
    ("from astroid.node_classes import *", DeprecationWarning, ASTROID_WARNING),
    ("import tests.samples.warnings_module", DeprecationWarning, "mod warn"),
    ("from tests.samples.warnings_module import fun", DeprecationWarning, "mod warn"),
    ("from tests.samples.warnings_function import func", DeprecationWarning, "func warn"),
])
def test_finder__import(given, etype, emsg):
    r = e(p(given))
    assert r == [(etype, emsg)]
