import warnings

warnings.warn("mod warn", DeprecationWarning)


def func():
    pass


def not_imported_func():
    warnings.warn("this one is ignored")
