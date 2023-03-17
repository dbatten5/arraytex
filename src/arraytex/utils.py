"""Utils module."""

from functools import wraps
from typing import Callable
from typing import TypeVar

import pyperclip
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
