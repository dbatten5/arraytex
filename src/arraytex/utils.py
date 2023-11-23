"""Utils module."""
import re
from functools import wraps
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import TypeVar
from typing import Union

import numpy as np
import pyperclip
from numpy.typing import NDArray
from typing_extensions import ParamSpec


P = ParamSpec("P")
T = TypeVar("T")


def use_clipboard(func: Callable[P, T]) -> Callable[P, str]:
    """Augument decorated functions argument to copy the output to the clipboard."""

    @wraps(func)
    def wrapper_func(*args: P.args, **kwargs: P.kwargs) -> str:
        """Wrapped function."""
        out = func(*args, **kwargs)

        if kwargs.get("to_clp"):
            pyperclip.copy(out)
            print("ArrayTeX: copied to clipboard")

        return str(out)

    return wrapper_func


def _parse_lines(
    arr: NDArray[Any],
    num_format: Optional[str] = None,
    scientific_notation: bool = False,
) -> List[str]:
    formatter = {}
    if num_format:

        def num_formatter(x: Union[np.int64, np.float64, np.float32]) -> str:
            return f"%{num_format}" % x

        formatter.update({"float_kind": num_formatter, "int_kind": num_formatter})

    lines = (
        np.array2string(
            arr,
            max_line_width=np.inf,  # type: ignore
            formatter=formatter,  # type: ignore
            separator=" & ",
        )
        .replace("[", "")
        .replace("]", "")
        .replace(" &\n", "\n")
    )

    if num_format and "e" in num_format:
        pattern = r"e([\+-]?\d+)"
        replace = r"\\mathrm{e}{\g<1>}"
        if scientific_notation:
            replace = r" \\times 10^{\g<1>}"
        lines = re.sub(pattern, replace, lines)

    return lines.splitlines()
