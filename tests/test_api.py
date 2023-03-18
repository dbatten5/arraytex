"""Tests for the main API."""
from unittest import mock
from unittest.mock import MagicMock

import numpy as np
import pytest

from arraytex.api import to_matrix
from arraytex.api import to_tabular
from arraytex.errors import DimensionMismatchError
from arraytex.errors import TooManyDimensionsError


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

    def test_one_d(self) -> None:
        """One dimensional vectors are handled correctly."""
        mat = np.array([1, 2, 3])

        out = to_matrix(mat)

        assert (
            out
            == r"""\begin{bmatrix}
1 & 2 & 3 \\
\end{bmatrix}"""
        )

    def test_0_d(self) -> None:
        """0 dimensional vectors are handled correctly."""
        mat = np.array(1)

        out = to_matrix(mat)

        assert (
            out
            == r"""\begin{bmatrix}
1 \\
\end{bmatrix}"""
        )

    def test_3_d(self) -> None:
        """>2 dimensional arrays are handled correctly."""
        mat = np.arange(8).reshape(2, 2, 2)

        with pytest.raises(TooManyDimensionsError):
            to_matrix(mat)


class TestClipboard:
    """Tests for the `to_clp` arg."""

    @mock.patch("arraytex.utils.pyperclip", autospec=True)
    def test_success(self, mock_pyperclip: MagicMock) -> None:
        """Outputs are copied to the clipboard."""
        mat = np.array(1)

        to_matrix(mat, to_clp=True)

        mock_pyperclip.copy.assert_called_once_with(
            "\\begin{bmatrix}\n1 \\\\\n\\end{bmatrix}"
        )


class TestToTabular:
    """Tests for the `to_tabular` function."""

    def test_too_many_dimensions(self) -> None:
        """Error is thrown for too many dimensions."""
        mat = np.arange(8).reshape(2, 2, 2)

        with pytest.raises(TooManyDimensionsError):
            to_tabular(mat)

    def test_mismatch_col_align(self) -> None:
        """Error is thrown if wrong number of col_align items."""
        mat = np.arange(6).reshape(2, 3)

        with pytest.raises(DimensionMismatchError) as exc:
            to_tabular(mat, col_align=["c", "c"])

        assert str(exc.value) == (
            "Number of `col_align` items doesn't match number of "
            + "columns (2 against 3)"
        )

    def test_mismatch_cols(self) -> None:
        """Error is thrown if wrong number of cols items."""
        mat = np.arange(6).reshape(2, 3)

        with pytest.raises(DimensionMismatchError) as exc:
            to_tabular(mat, cols=["1", "2"])

        assert str(exc.value) == (
            "Number of `cols` items doesn't match number of " + "columns (2 against 3)"
        )

    def test_default(self) -> None:
        """A formatted matrix is returned."""
        mat = np.arange(1, 7).reshape(2, 3)

        out = to_tabular(mat)

        assert (
            out
            == r"""\begin{tabular}{c c c}
\toprule
Col 1 & Col 2 & Col 3 \\
\midrule
1 & 2 & 3 \\
4 & 5 & 6 \\
\endrule
\end{tabular}"""
        )

    def test_given_cols(self) -> None:
        """User can supply col names."""
        mat = np.arange(1, 5).reshape(2, 2)

        out = to_tabular(mat, cols=["1", "b"])

        assert (
            out
            == r"""\begin{tabular}{c c}
\toprule
1 & b \\
\midrule
1 & 2 \\
3 & 4 \\
\endrule
\end{tabular}"""
        )

    def test_given_col_align(self) -> None:
        """User can supply col_align list."""
        mat = np.arange(1, 5).reshape(2, 2)

        out = to_tabular(mat, col_align=["l", "r"])

        assert (
            out
            == r"""\begin{tabular}{l r}
\toprule
Col 1 & Col 2 \\
\midrule
1 & 2 \\
3 & 4 \\
\endrule
\end{tabular}"""
        )

    def test_one_dimensional(self) -> None:
        """One dimensinal vectors are expanded properly."""
        mat = np.arange(1, 4)

        out = to_tabular(mat)

        assert (
            out
            == r"""\begin{tabular}{c c c}
\toprule
Col 1 & Col 2 & Col 3 \\
\midrule
1 & 2 & 3 \\
\endrule
\end{tabular}"""
        )

    def test_0_d(self) -> None:
        """0 dimensional scalars are handled properly."""
        mat = np.array(1)

        out = to_tabular(mat)

        assert (
            out
            == r"""\begin{tabular}{c}
\toprule
Col 1 \\
\midrule
1 \\
\endrule
\end{tabular}"""
        )
