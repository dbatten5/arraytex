# Usage

<!-- ```{eval-rst} -->
<!-- .. click:: arraytex.__main__:main -->
<!--     :prog: arraytex -->
<!--     :nested: full -->
<!-- ``` -->

Suppose you want to convert a `numpy.NDArray` object to a LaTeX representation:

```python
>>> import numpy as np
>>> A = np.arange(1, 7).reshape(2, 3)
>>> A
array([[1, 2, 3],
       [4, 5, 6]])
```

## To matrix

Basic usage:

```python
>>> from arraytex import to_matrix
>>> print(to_matrix(A))
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{bmatrix}
```

Different matrix style environment delimiters can be used:

```python
>>> print(to_matrix(A, style="p"))
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix}
```

So can builtin number formatters:

```python
>>> print(to_matrix(A * 1e3, num_format=".2e"))
\begin{bmatrix}
1.00\mathrm{e}{+03} & 2.00\mathrm{e}{+03} & 3.00\mathrm{e}{+03} \\
4.00\mathrm{e}{+03} & 5.00\mathrm{e}{+03} & 6.00\mathrm{e}{+03} \\
\end{bmatrix}
```

Prefer scientific notation to e-notation? No problem:

```python
>>> print(to_matrix(A * 1e3, num_format=".2e", scientific_notation=True))
\begin{bmatrix}
1.00 \times 10^{+03} & 2.00 \times 10^{+03} & 3.00 \times 10^{+03} \\
4.00 \times 10^{+03} & 5.00 \times 10^{+03} & 6.00 \times 10^{+03} \\
\end{bmatrix}
```

## To tabular

Basic usage:

```python
>>> from arraytex import to_tabular
>>> print(to_tabular(A))
\begin{tabular}{c c c}
\toprule
Col 1 & Col 2 & Col 3 \\
\midrule
1 & 2 & 3 \\
4 & 5 & 6 \\
\bottomrule
\end{tabular}
```

The `num_format` and `scientific_notation` arguments are available to use:

```python
>>> print(to_tabular(A, num_format=".2f"))
\begin{tabular}{c c c}
\toprule
Col 1 & Col 2 & Col 3 \\
\midrule
1.00 & 2.00 & 3.00 \\
4.00 & 5.00 & 6.00 \\
\bottomrule
\end{tabular}
```

You can pass custom column names and column align identifiers:

```python
>>> print(to_tabular(A, col_align=["l", "c", "r"], col_names=["Data", "More Data", "Even More Data"]))
\begin{tabular}{l c r}
\toprule
Data & More Data & Even More Data \\
\midrule
1 & 2 & 3 \\
4 & 5 & 6 \\
\bottomrule
\end{tabular}
```

Pass a list of row identifiers to be used as a table index:

```python
>>> print(to_tabular(A, index=["Sample 1", "Sample 2"]))
\begin{tabular}{l c c c}
\toprule
Index & Col 1 & Col 2 & Col 3 \\
\midrule
Sample 1 & 1 & 2 & 3 \\
Sample 2 & 4 & 5 & 6 \\
\bottomrule
\end{tabular}
```

Specify the name of the index column through `col_names`:

```python
>>> print(to_tabular(A, index=["Sample 1", "Sample 2"], col_names=["Which Sample", "A", "B", "C"]))
\begin{tabular}{l c c c}
\toprule
Which Sample & A & B & C \\
\midrule
Sample 1 & 1 & 2 & 3 \\
Sample 2 & 4 & 5 & 6 \\
\bottomrule
\end{tabular}
```
