# notice

Python linter that warns you about using deprecated modules, classes, and functions. It provides a CLI as well as [flake8][flake8] and [pylint][pylint] plugins.

## Usage

Installation:

```bash
python3 -m pip install notice
```

Now, you can use it in one of the following ways:

1. Directly from CLI: `python3 -m notice ./my_project/`
1. As a [flake8][flake8] plugin. Just run `flake8 ./my_project/`, it will automatically detect the plugin.
1. As a [pylint][pylint] plugin. For pylint, plugins must be explicitly specified: `pylint --load-plugins=notice ./my_project/`.

[flake8]: https://flake8.pycqa.org/en/latest/
[pylint]: https://pylint.org/
