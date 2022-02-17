# flake8_warnings

Python linter that warns you about using deprecated modules, classes, and functions. It provides a CLI as well as [flake8][flake8] and [pylint][pylint] plugins.

## Usage

Installation:

```bash
python3 -m pip install flake8_warnings
```

Now, you can use it in one of the following ways:

1. Directly from CLI: `python3 -m flake8_warnings ./my_project/`
1. As a [flake8][flake8] plugin. Just run `flake8 ./my_project/`, it will automatically detect the plugin.
1. As a [pylint][pylint] plugin. For pylint, plugins must be explicitly specified: `pylint --load-plugins=flake8_warnings ./my_project/`.

[flake8]: https://flake8.pycqa.org/en/latest/
[pylint]: https://pylint.org/
