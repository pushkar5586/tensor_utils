"""Sphinx configuration for tensor_utils."""

import os
import sys

# Make the package importable without needing `pip install -e .` first.
# conf.py lives in sphinx_docs/, the package source lives in ../src.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

project = "tensor_utils"
copyright = "2026, Pushkar Agrawal"
author = "Pushkar Agrawal"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",      # pulls docstrings from your code
    "sphinx.ext.napoleon",     # lets autodoc understand Google/NumPy style docstrings
    "sphinx.ext.viewcode",     # adds a "view source" link per documented object
    "sphinx.ext.intersphinx",  # lets you link out to numpy's own docs by name
]

# Napoleon settings: your docstrings are Google-style.
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True

# Show parameter/return types inline in the description rather than a
# separate signature block — reads more like prose.
autodoc_typehints = "description"
autodoc_member_order = "bysource"

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
}

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "furo"
html_static_path = ["_static"]
html_title = "tensor_utils"
