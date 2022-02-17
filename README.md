# flake8-warnings

Python linter that warns you about using deprecated modules, classes, and functions. It provides a CLI as well as [flake8][flake8] and [pylint][pylint] plugins.

## Usage

Installation:

```bash
python3 -m pip install flake8-warnings
```

Now, you can use it in one of the following ways:

1. Directly from CLI: `python3 -m flake8_warnings ./my_project/`
1. As a [flake8][flake8] plugin. Just run `flake8 ./my_project/`, it will automatically detect the plugin.
1. As a [pylint][pylint] plugin. For pylint, plugins must be explicitly specified: `pylint --load-plugins=flake8_warnings ./my_project/`.

[flake8]: https://flake8.pycqa.org/en/latest/
[pylint]: https://pylint.org/

## How it works

It analyzes all imported modules, classes and functions and detects the following:

1. [warnings.warn](https://docs.python.org/3/library/warnings.html#warnings.warn) function calls.
1. Deprecation decorators like [deprecated](https://github.com/tantale/deprecated) or [deprecation](https://github.com/briancurtin/deprecation).
1. Deprecation messages in docstrings.

## License

1. flake8-wranings is licensed under [MIT License](./LICENSE). On practice, I don't care how you're going to use it. i did the project because it is fun, not because I want to be famous or whatever.
1. [astroid](https://github.com/PyCQA/astroid) is a direct runtime dependency of flake8-warning and it is licensed under [LGPL-2.1 License](https://github.com/PyCQA/astroid/blob/main/LICENSE). It allows commercial and private usage, distribution and whatever, don't confuse it with GPL. However, if your legal department is still nervous, just don't make flake8-warnings a production dependency (why would you?), use it only on dev and test environments.
