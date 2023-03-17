"""Main package API."""

import re
from typing import Any
from typing import Optional
from typing import Union

import numpy as np
from numpy.typing import NDArray

from .errors import TooManyDimensionsError
from .utils import use_clipboard


@use_clipboard
def to_matrix(
    arr: NDArray[Any],
    style: str = "b",
    num_format: Optional[str] = None,
    scientific_notation: bool = False,
    to_clp: bool = False,
) -> str:
    """Convert a numpy.NDArray to LaTeX matrix.

    Args:
        arr: the array to be converted
        style: a style formatter string, either "b" for "bmatrix" or "p" for "pmatrix"
        num_format: a number formatter string, e.g. ".2f"
        scientific_notation: a flag to determine whether 1 x 10^3 should be used,
            otherwise e-notation is used (1e3)
        to_clp: copy the output to the system clipboard

    Returns:
        the string representation of the array

    Raises:
        TooManyDimensionsError: when the supplied array has more than 2 dimensions
    """
    if len(arr.shape) > 2:
        raise TooManyDimensionsError

    environment = f"{style}matrix"

    formatter = {}
    if num_format:

        def num_formatter(x: Union[np.int64, np.float64, np.float32]) -> str:
            return f"%{num_format}" % x

        formatter.update({"float_kind": num_formatter, "int_kind": num_formatter})

    lines = (
        np.array2string(
            arr,
            max_line_width=np.inf,  # type: ignore  # noqa
            formatter=formatter,  # type: ignore  # noqa
            separator=" & ",
        )
        .replace("[", "")
        .replace("]", "")
        .replace(" &\n", "\n")
    )

    if num_format and "e" in num_format:
        pattern = r"e(-?\d+)"
        replace = r"\\mathrm{e}{\g<1>}"
        if scientific_notation:
            replace = r" \\times 10^{\g<1>}"
        lines = re.sub(pattern, replace, lines)

    rv = [f"\\begin{{{environment}}}"]
    rv += [line.strip() + r" \\" for line in lines.splitlines()]
    rv += [f"\\end{{{environment}}}"]

    return "\n".join(rv)
