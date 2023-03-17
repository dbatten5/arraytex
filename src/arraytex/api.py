"""Main package API."""
import re
from typing import Any
from typing import Optional
from typing import Union

import numpy as np
from numpy.typing import NDArray


def to_matrix(
    arr: NDArray[Any],
    style: str = "b",
    num_format: Optional[str] = None,
) -> str:
    """Convert a numpy.NDArray to LaTeX matrix.

    Args:
        arr: the array to be converted
        style: a style formatter string, either "b" for "bmatrid" or "p" for "pmatrix"
        num_format: a number formatter string, e.g. ".2f"

    Returns:
        the string representation of the array
    """

    def num_formatter(x: Union[int, float]) -> str:
        return f"%{num_format}" % x

    environment = f"{style}matrix"

    formatter = {}
    if num_format:
        formatter.update({"float_kind": num_formatter, "int_kind": num_formatter})

    lines = (
        np.array2string(arr, max_line_width=np.inf, formatter=formatter)  # type: ignore  # noqa
        .replace("[", "")
        .replace("]", "")
    )

    if num_format and "e" in num_format:
        pattern = r"e(-?\d+)"
        replace = r"\\mathrm{e}{\g<1>}"
        lines = re.sub(pattern, replace, lines)

    rv = [f"\\begin{{{environment}}}"]
    rv += ["  " + " & ".join(line.split()) + r" \\" for line in lines.splitlines()]
    rv += [f"\\end{{{environment}}}"]

    return "\n".join(rv)
