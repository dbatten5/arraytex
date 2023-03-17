"""Main package API."""

from typing import Any

import numpy as np
from numpy.typing import NDArray


def to_matrix(arr: NDArray[Any]) -> str:
    """Convert a numpy.NDArray to LaTeX matrix.

    Args:
        arr: the array to be converted

    Returns:
        the string representation of the array
    """
    environment = "bmatrix"
    lines = (
        np.array2string(arr, max_line_width=np.inf)  # type: ignore  # noqa
        .replace("[", "")
        .replace("]", "")
        .splitlines()
    )
    rv = [f"\\begin{{{environment}}}"]
    rv += ["  " + " & ".join(line.split()) + r" \\" for line in lines]
    rv += [f"\\end{{{environment}}}"]
    return "\n".join(rv)
