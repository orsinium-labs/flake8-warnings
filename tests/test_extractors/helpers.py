from __future__ import annotations

from textwrap import dedent

import astroid

from flake8_warnings._extractors import Extractor


def p(text) -> astroid.Module:
    """Parse the text into astroid tree, print it.
    """
    tree = astroid.parse(dedent(text))
    print(tree.repr_tree())
    return tree


def e(extractor: type[Extractor], node: astroid.NodeNG) -> list[tuple[type, str]]:
    return [(w.category, w.message) for w in extractor().extract(node)]
