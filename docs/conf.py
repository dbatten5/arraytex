"""Sphinx configuration."""
project = "ArrayTeX"
author = "Dom Batten"
copyright = "2023, Dom Batten"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
