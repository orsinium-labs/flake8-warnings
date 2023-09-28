import warnings


def func():
    warnings.warn('func warn', DeprecationWarning)
    return 1
    warnings.warn('this one is ignored')  # type: ignore


def not_imported_func():
    warnings.warn('this one is ignored')
