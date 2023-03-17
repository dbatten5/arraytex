"""Module to hold custom errors."""


class TooManyDimensionsError(Exception):
    """Raised when an array of more than 2 dimensions is supplied."""


class DimensionMismatchError(Exception):
    """Raised when dimensionality issues occur."""
