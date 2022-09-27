import pytest

from flake8_warnings._finder import WarningFinder

from .helpers import p


@pytest.mark.parametrize('given', [
    # PEP 594: Removing dead batteries
    'import aifc',
    'import asynchat',
    'import asyncore',
    'import audioop',
    'import cgi',
    'import cgitb',
    'import chunk',
    'import crypt',
    'import imghdr',
    'import mailcap',
    # 'import msilib',  # available only on windows
    'import nntplib',
    'import nis',
    'import ossaudiodev',
    'import pipes',
    'import smtpd',
    'import sndhdr',
    'import spwd',
    'import sunau',
    'import telnetlib',
    'import uu',
    'import xdrlib',

    'import optparse',
    'import tkinter.tix',
    'import xml.etree.cElementTree',

    # from-import
    'from smtpd import SMTPServer',
])
def test_module_deprecated(given):
    finder = WarningFinder(p(given))
    r = [(w.category, w.message) for w in finder.find()]
    assert len(r) == 1
    assert r[0][0] is DeprecationWarning
