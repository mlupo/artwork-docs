# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

master_doc = 'index'
project = u'The Max Lupo Artwork Documentation Archive'
copyright = u'CC-BY-SA, Max Lupo, 2018'

# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

# intersphinx_mapping = {
#     "rtd": ("https://docs.readthedocs.io/en/stable/", None),
#     "python": ("https://docs.python.org/3/", None),
#     "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
# }
# intersphinx_disabled_domains = ["std"]
# 
# templates_path = ["_templates"]
# 
# # -- Options for EPUB output
# epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# extensions = [
#     'recommonmark',
#     'sphinx_rtd_theme',
# ]
# 
# html_theme = "sphinx_rtd_theme"
# 
# source_suffix = ['.rst', '.md']
# 
# master_doc = 'index'
# project = u'The Max Lupo Artwork Documentation Archive'
# copyright = u'CC-BY-SA, Max Lupo, 2018'
# 
# # -- Options for Epub output ----------------------------------------------
# 
# # Bibliographic Dublin Core info.
# epub_title = u'The Max Lupo Artwork Documentation Archive'
# epub_author = u'Max Lupo'
# epub_publisher = u'Max Lupo'
# epub_copyright = u'2018, Max Lupo'
# 
# # def setup(app):
# #     app.add_stylesheet('css/resize.css')
