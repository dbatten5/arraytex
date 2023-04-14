# Usage

<!-- ```{eval-rst} -->
<!-- .. click:: arraytex.__main__:main -->
<!--     :prog: arraytex -->
<!--     :nested: full -->
<!-- ``` -->

Suppose you want to convert a `numpy.NDArray` object to a LaTeX representation:

```python
>>> import numpy as np
>>> A = np.arange(6).reshape(2, 3)
>>> A
array([[0, 1, 2],
       [3, 4, 5]])
```

## To matrix

First import the `to_matrix` function:

```python
>>> from arraytex import to_matrix
```

Then run `to_matrix` with a `numpy.NDArray` object as the first argument:

```python
>>> print(to_matrix(A))
\begin{bmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
\end{bmatrix}
```

Different matrix style environment delimiters can be used:

```python
>>> print(to_matrix(A, style="p"))
\begin{pmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
\end{pmatrix}
```

So can builtin number formatters:

```python
>>> print(to_matrix((A + 1) * 1e3, num_format=".2e"))
\begin{bmatrix}
1.00\mathrm{e}{+03} & 2.00\mathrm{e}{+03} & 3.00\mathrm{e}{+03} \\
4.00\mathrm{e}{+03} & 5.00\mathrm{e}{+03} & 6.00\mathrm{e}{+03} \\
\end{bmatrix}
```

Prefer scientific notation to e-notation? No problem:

```python
>>> print(to_matrix((A + 1) * 1e3, num_format=".2e", scientific_notation=True))
\begin{bmatrix}
1.00 \times 10^{+03} & 2.00 \times 10^{+03} & 3.00 \times 10^{+03} \\
4.00 \times 10^{+03} & 5.00 \times 10^{+03} & 6.00 \times 10^{+03} \\
\end{bmatrix}
```

## To tabular

First import the `to_tabular` function:

```python
>>> from arraytex import to_tabular
```

Then run `to_tabular` with a `numpy.NDArray` as the first argument:

```python
>>> print(to_tabular(A))
\begin{tabular}{c c c}
\toprule
Col 1 & Col 2 & Col 3 \\
\midrule
0 & 1 & 2 \\
3 & 4 & 5 \\
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
0.00 & 1.00 & 2.00 \\
3.00 & 4.00 & 5.00 \\
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
0 & 1 & 2 \\
3 & 4 & 5 \\
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
Sample 1 & 0 & 1 & 2 \\
Sample 2 & 3 & 4 & 5 \\
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
Sample 1 & 0 & 1 & 2 \\
Sample 2 & 3 & 4 & 5 \\
\bottomrule
\end{tabular}
```
