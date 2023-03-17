"""Utils module."""

from functools import wraps
from typing import Any
from typing import Callable
from typing import TypeVar
from typing import cast

import pyperclip


F = TypeVar("F", bound=Callable[..., str])


def use_clipboard(func: F) -> F:
    """Augument decorated functions argument to copy the output to the clipboard."""

    @wraps(func)
    def wrapper_func(*args: Any, **kwargs: Any) -> str:
        """Wrapped function."""
        out = func(*args, **kwargs)

        if kwargs.get("to_clp"):
            pyperclip.copy(out)
            print("ArrayTeX: copied to clipboard")

        return out

    return cast(F, wrapper_func)
