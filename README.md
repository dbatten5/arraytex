# ArrayTeX

[![PyPI](https://img.shields.io/pypi/v/arraytex.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/arraytex.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/arraytex)][python version]
[![License](https://img.shields.io/pypi/l/arraytex)][license]

[![Read the documentation at https://arraytex.readthedocs.io/](https://img.shields.io/readthedocs/arraytex/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/dbatten5/arraytex/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/dbatten5/arraytex/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/arraytex/
[status]: https://pypi.org/project/arraytex/
[python version]: https://pypi.org/project/arraytex
[read the docs]: https://arraytex.readthedocs.io/
[tests]: https://github.com/dbatten5/arraytex/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/dbatten5/arraytex
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

Convert a `numpy.NDArray` to various LaTeX forms.

```python
>>> import numpy as np
>>> import arraytex as atx
>>> A = np.array([[1, 2, 3], [4, 5, 6]])
>>> print(atx.to_matrix(A))
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{bmatrix}
```

Inspired by [@josephcslater](https://github.com/josephcslater)'s
[array_to_latex](https://github.com/josephcslater/array_to_latex).

## Features

- Support for different environment delimiters (`bmatrix` or `pmatrix`) and different
  number formatters (`:.2f`, `:.3e`, etc.).
- Fully tested and typed.

## Requirements

- `python >= 3.8`

## Installation

You can install _ArrayTeX_ via [pip] from [PyPI]:

```console
$ pip install arraytex
```

## Usage

Please see the [docs](https://arraytex.readthedocs.io/) for more information.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_ArrayTeX_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/dbatten5/arraytex/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/dbatten5/arraytex/blob/main/LICENSE
[contributor guide]: https://github.com/dbatten5/arraytex/blob/main/CONTRIBUTING.md
[command-line reference]: https://arraytex.readthedocs.io/en/latest/usage.html
