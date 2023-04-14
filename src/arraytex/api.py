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
        style: a style formatter string, such as "b" for "bmatrix" or "p" for "pmatrix"
        num_format: a number formatter string, e.g. ".2f"
        scientific_notation: a flag to determine whether e.g. 1 x 10^3 format should
            be used if ".e" is used for `num_format`, otherwise e-notation (1e3)
            is used
        to_clp: copy the output to the system clipboard

    Returns:
        the LaTeX matrix string representation of the array

    Raises:
        TooManyDimensionsError: when the supplied array has more than 2 dimensions
    """
    if len(arr.shape) > 2:
        raise TooManyDimensionsError

    lines = _parse_lines(arr, num_format, scientific_notation)

    environment = f"{style}matrix"

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
    col_names: Optional[List[str]] = None,
    index: Optional[List[str]] = None,
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
        col_names: an optional list of column names, otherwise generic names will be assigned
        index: an optional table index, i.e. row identifiers
        to_clp: copy the output to the system clipboard

    Returns:
        the LaTeX tabular string representation of the array

    Raises:
        TooManyDimensionsError: when the supplied array has more than 2 dimensions
        DimensionMismatchError: when there is a mismatch between column items and number
            of columns, or column index items and number of rows
    """
    n_dims = len(arr.shape)

    if n_dims == 0:
        n_cols = 1
    elif n_dims == 1:
        n_cols = arr.shape[0]
    elif n_dims == 2:
        n_cols = arr.shape[1]
    else:
        raise TooManyDimensionsError

    if not index:
        if isinstance(col_align, list) and len(col_align) != n_cols:
            raise DimensionMismatchError(
                f"Number of `col_align` items ({len(col_align)}) "
                + f"doesn't match number of columns ({n_cols})"
            )

        if col_names and len(col_names) != n_cols:
            raise DimensionMismatchError(
                f"Number of `col_names` items ({len(col_names)}) "
                + f"doesn't match number of columns ({n_cols})"
            )

    if (
        index
        and col_names
        and isinstance(col_align, list)
        and len(col_names) != len(col_align)
    ):
        raise DimensionMismatchError(
            f"Number of `col_align` items ({len(col_align)}) "
            + f"doesn't match number of columns ({len(col_names)})"
        )

    if isinstance(col_align, str):
        col_align = [col_align for _ in range(n_cols)]

    if not col_names:
        col_names = [f"Col {i + 1}" for i in range(n_cols)]

    lines = _parse_lines(arr, num_format, scientific_notation)

    if index:
        if len(index) != len(lines):
            raise DimensionMismatchError(
                f"Number of `index` items ({len(index)}) "
                + f"doesn't match number of rows ({len(lines)})"
            )

        if len(col_align) == n_cols:
            col_align.insert(0, "l")

        if len(col_names) == n_cols:
            col_names.insert(0, "Index")

        for idx, line in enumerate(lines):
            lines[idx] = f"{index[idx]} & " + line.strip()

    rv = [f"\\begin{{tabular}}{{{' '.join(col_align)}}}"]
    rv += [r"\toprule"]
    rv += [" & ".join(col_names) + r" \\"]
    rv += [r"\midrule"]
    rv += [line.strip() + r" \\" for line in lines]
    rv += [r"\bottomrule"]
    rv += [r"\end{tabular}"]

    return "\n".join(rv)
