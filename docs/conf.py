#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/main/config
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys

# This is for pyvista
os.system("/usr/bin/Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &")
os.environ["DISPLAY"] = ":99"
os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["PYVISTA_USE_IPYVTK"] = "true"


# Location of Sphinx files
sys.path.insert(0, os.path.abspath("./../"))  ##Add the folder one level above
os.environ[
    "SPHINX_APIDOC_OPTIONS"
] = "members,show-inheritance"  ## Hide undocumented members
import sphinx.ext.apidoc

# from sphinx_gallery.sorting import FileNameSortKey

# pio.renderers.default = "sphinx_gallery"

autodoc_default_options = {
    "private-members": False,
    "inherited-members": True,
}


def setup(app):
    app.add_css_file("css/stylesheet.css")
    app.add_js_file("webcode/summaryOpen.js")
    sphinx.ext.apidoc.main(
        [
            "-f",  # Overwrite existing files
            "-T",  # Create table of contents
            "-e",  # Give modules their own pages
            "-E",  # user docstring headers
            "-M",  # Modules first
            "-o",  # Output the files to:
            "./_autogen/",  # Output Directory
            "./../magpylib",  # Main Module directory
        ]
    )


# -- Project information -----------------------------------------------------

project = "Magpylib"
copyright = "2022, SAL - Silicon Austria Labs"
author = "Michael Ortner <magpylib@gmail.com>"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
from magpylib import __version__ as release


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "4.4.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.autosummary",
    "sphinx.ext.ifconfig",
    "matplotlib.sphinxext.plot_directive",
    # "nbsphinx",
    # "sphinx_gallery.load_style",
    "sphinx_copybutton",
    "myst_nb",
    "sphinx_thebe",
    # "myst_parser",
    # "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README*"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

html_logo = "./_static/images/magpylib_logo.png"
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "repository_url": "https://github.com/magpylib/magpylib",
    "path_to_docs": "docs/",
    "repository_branch": release,
    "use_repository_button": True,
    "use_download_button": True,
    "launch_buttons": {"binderhub_url": "https://mybinder.org", "thebe": True},
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "magpylibdoc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    "extraclassoptions": "openany,oneside"  # Remove empty pages from .PDF download
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "magpylib.tex", "magpylib Documentation", "Michael Ortner", "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "magpylib", "magpylib Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "magpylib",
        "magpylib Documentation",
        author,
        "magpylib",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

# -- Markdown enable

source_suffix = [".rst", ".md"]

# html_js_files = [
#    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"
# ]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
    "https://unpkg.com/thebe@latest/lib/index.js",
]

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML"
mathjax2_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "processEscapes": True,
        "ignoreClass": "document",
        "processClass": "math|output_area",
    }
}

# needed for sphinx >= 4.3
mathjax_options = {
    "async": "async",
}

myst_update_mathjax = False
