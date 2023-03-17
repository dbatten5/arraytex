"""Tests for the main API."""
import numpy as np

from arraytex.api import to_matrix


class TestToMatrix:
    """Tests for the `to_matrix` function."""

    def test_success(self) -> None:
        """A formatted matrix is returned."""
        mat = np.array(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )

        out = to_matrix(mat)

        assert (
            out
            == r"""\begin{bmatrix}
  1 & 2 & 3 \\
  4 & 5 & 6 \\
\end{bmatrix}"""
        )
