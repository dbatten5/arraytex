"""Main package API."""

from typing import Any
from typing import List
from typing import Optional
from typing import Union

from numpy.typing import NDArray

from .errors import DimensionMismatchError
from .errors import TooManyDimensionsError
from .utils import _parse_lines
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

    lines = _parse_lines(arr, num_format, scientific_notation)

    rv = [f"\\begin{{{environment}}}"]
    rv += [line.strip() + r" \\" for line in lines]
    rv += [f"\\end{{{environment}}}"]

    return "\n".join(rv)


@use_clipboard
def to_tabular(
    arr: NDArray[Any],
    num_format: Optional[str] = None,
    scientific_notation: bool = False,
    col_align: Union[List[str], str] = "c",
    cols: Optional[List[str]] = None,
    to_clp: bool = False,
) -> str:
    """Convert a numpy.NDArray to LaTeX tabular environment.

    Args:
        arr: the array to be converted
        num_format: a number formatter string, e.g. ".2f"
        scientific_notation: a flag to determine whether 1 x 10^3 should be used,
            otherwise e-notation is used (1e3)
        col_align: set the alignment of the columns, usually "c", "r" or "l". If a
            single character is provided then it will be broadcast to all columns. If a list
            is provided then each item will be assigned to each column, list size and
            number of columns must match
        cols: an optional list of column names, otherwise generic names will be assigned
        to_clp: copy the output to the system clipboard

    Returns:
        the string representation of the array

    Raises:
        TooManyDimensionsError: when the supplied array has more than 2 dimensions
    """
    if len(arr.shape) == 1:
        n_cols = arr.shape[0]
    elif len(arr.shape) == 2:
        n_cols = arr.shape[1]
    else:
        raise TooManyDimensionsError

    if isinstance(col_align, list) and len(col_align) != n_cols:
        raise DimensionMismatchError(
            "Number of `col_align` items doesn't match number of columns "
            + f"({len(col_align)} against {n_cols})"
        )

    if isinstance(col_align, str):
        col_align = [col_align for _ in range(n_cols)]

    if cols and len(cols) != n_cols:
        raise DimensionMismatchError(
            "Number of `cols` items doesn't match number of columns "
            + f"({len(cols)} against {n_cols})"
        )

    if not cols:
        cols = [f"Col {i + 1}" for i in range(n_cols)]

    lines = _parse_lines(arr, num_format, scientific_notation)

    rv = [f"\\begin{{tabular}}{{{' '.join(col_align)}}}"]
    rv += [r"\toprule"]
    rv += [" & ".join(cols) + r" \\"]
    rv += [r"\midrule"]
    rv += [line.strip() + r" \\" for line in lines]
    rv += [r"\endrule"]
    rv += [r"\end{tabular}"]

    return "\n".join(rv)
