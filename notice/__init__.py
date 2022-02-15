"""Linter (flake8, pylint, custom CLI) for finding usage of deprecated functions.
"""

from ._flake8_plugin import Flake8Checker


__version__ = '0.1.0'
__all__ = ['Flake8Checker']
