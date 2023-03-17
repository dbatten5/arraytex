"""Tests for the main API."""
import numpy as np

from arraytex.api import to_matrix


class TestToMatrix:
    """Tests for the `to_matrix` function."""

    def test_default(self) -> None:
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

    def test_style(self) -> None:
        """An arg can be supplied to determine the style of the returned matrix."""
        mat = np.array(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )

        out = to_matrix(mat, style="p")

        assert (
            out
            == r"""\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix}"""
        )

    def test_decimal_format(self) -> None:
        """Decimal style of number formatting can be selected."""
        mat = np.array(
            [
                [1, 2, 3],
                [4, 5, 6],
            ]
        )

        out = to_matrix(mat, num_format=".2f")

        assert (
            out
            == r"""\begin{bmatrix}
1.00 & 2.00 & 3.00 \\
4.00 & 5.00 & 6.00 \\
\end{bmatrix}"""
        )

    def test_e_notation(self) -> None:
        """Scientific E notation can be selected."""
        mat = np.array(
            [
                [0.001, 0.002, 0.003],
                [0.004, 0.005, 0.006],
            ]
        )

        out = to_matrix(mat, num_format=".2e")

        assert (
            out
            == r"""\begin{bmatrix}
1.00\mathrm{e}{-03} & 2.00\mathrm{e}{-03} & 3.00\mathrm{e}{-03} \\
4.00\mathrm{e}{-03} & 5.00\mathrm{e}{-03} & 6.00\mathrm{e}{-03} \\
\end{bmatrix}"""
        )

    def test_scientific_notation(self) -> None:
        """Scientific  can be selected."""
        mat = np.array(
            [
                [0.001, 0.002, 0.003],
                [0.004, 0.005, 0.006],
            ]
        )

        out = to_matrix(mat, num_format=".2e", scientific_notation=True)

        assert (
            out
            == r"""\begin{bmatrix}
1.00 \times 10^{-03} & 2.00 \times 10^{-03} & 3.00 \times 10^{-03} \\
4.00 \times 10^{-03} & 5.00 \times 10^{-03} & 6.00 \times 10^{-03} \\
\end{bmatrix}"""
        )
