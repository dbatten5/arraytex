"""Sphinx configuration."""
project = "ArrayTeX"
author = "Dom Batten"
copyright = "2023, Dom Batten"  # noqa: A001
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
