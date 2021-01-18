# .. Copyright (C) 2012-2020 Bryan A. Jones.
#
#   This file is part of the CodeChat system.
#
#   The CodeChat system is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   The CodeChat system is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied warranty
#   of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with the CodeChat system.  If not, see
#   <http://www.gnu.org/licenses/>.
#
# ***********************************************************
# |docname| - The CodeChat system documentation configuration
# ***********************************************************
# This file configures Sphinx, which transforms restructured text (reST) into
# html. See Sphinx `build configuration file docs
# <http://sphinx-doc.org/config.html>`_ for more information on the settings
# below.
#
# This file was originally created by sphinx-quickstart, then modified by hand.
# Notes on its operation:
#
# * This file is ``execfile()``\d by Sphinx with the current directory set to
#   its containing dir.
# * Not all possible configuration values are present in this autogenerated
#   file.
# * All configuration values have a default; values that are commented out serve
#   to show the default.
#
# Contents
# ========
# The following files also configure the documentation.
#
# .. toctree::
#   :maxdepth: 2
#
#   codechat_config.json
#   readthedocs.yml
#   docs/docs-requirements.txt


import sys, os
import CodeChat.CodeToRest

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, as shown here.
##sys.path.insert(0, os.path.abspath('.'))
#
# `Project information <http://sphinx-doc.org/config.html#project-information>`_
# ==============================================================================
# `project <http://sphinx-doc.org/config.html#confval-project>`_  and
# `copyright <http://sphinx-doc.org/config.html#confval-copyright>`_:
# General information about the project. **Change this** for your project.
project = "The CodeChat System"
copyright = "2020, Bryan A. Jones"

# The version info for the project you're documenting, acts as replacement for
# ``|version|`` and ``|release|``, also used in various other places throughout
# the built documents. **Change these** for your project.
#
# `version <http://sphinx-doc.org/config.html#confval-version>`_: The short X.Y
# version.
version = "1.0"
# `release <http://sphinx-doc.org/config.html#confval-release>`_: The full
# version, including alpha/beta/rc tags.
release = "version 1.0"

# There are two options for replacing ``|today|``:
#
# \1. If you set `today <http://sphinx-doc.org/config.html#confval-today>`_ to
# some non-false value, then it is used:
##today = ''
# \2. Otherwise, `today_fmt <http://sphinx-doc.org/config.html#confval-today_fmt>`_
# is used as the format for a strftime call.
##today_fmt = '%B %d, %Y'

# `highlight_language <http://sphinx-doc.org/config.html#confval-highlight_language>`_:
# The default language to highlight source code in.
highlight_language = "python3"

# `pygments_style <http://sphinx-doc.org/config.html#confval-pygments_style>`_:
# The style name to use for Pygments highlighting of source code.
pygments_style = "sphinx"

# `add_function_parentheses <http://sphinx-doc.org/config.html#confval-add_function_parentheses>`_:
# If true, '()' will be appended to ``:func:`` etc. cross-reference text.
##add_function_parentheses = True

# `add_module_names <http://sphinx-doc.org/config.html#confval-add_module_names>`_:
# If true, the current module name will be prepended to all description unit
# titles (such as ``.. function::``).
##add_module_names = True

# `show_authors <http://sphinx-doc.org/config.html#confval-show_authors>`_: If
# true, ``sectionauthor`` and ``moduleauthor`` directives will be shown in the
# output. They are ignored by default.
##show_authors = False

# `modindex_common_prefix <http://sphinx-doc.org/config.html#confval-modindex_common_prefix>`_:
# A list of ignored prefixes for module index sorting.
##modindex_common_prefix = []

#
# `General configuration <http://sphinx-doc.org/config.html#general-configuration>`_
# ==================================================================================
# `extensions <http://sphinx-doc.org/config.html#confval-extensions>`_: If your
# documentation needs a minimal Sphinx version, state it here.
##needs_sphinx = '1.5'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones. **CodeChat
# note:** The ``CodeChat.CodeToRestSphinx`` extension is mandatory; without it,
# CodeChat will not translate source code to reST and then (via Sphinx) to html.
extensions = ["CodeChat.CodeToRestSphinx", "sphinx.ext.graphviz", "recommonmark"]

# `templates_path <http://sphinx-doc.org/config.html#confval-templates_path>`_:
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# `rst_epilog <http://www.sphinx-doc.org/en/stable/config.html#confval-rst_epilog>`_:
# A string of reStructuredText that will be included at the end of every source
# file that is read.
rst_epilog = (
    # .. _docname substitution:
    #
    # ``|docname|`` substitution
    # --------------------------
    # Provide a convenient way to refer to a source file's name.
    """

.. |docname| replace:: :docname:`name`
"""

    # A commonly-used link.
    """
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/#imports
"""
)

# `source_suffix <http://sphinx-doc.org/config.html#confval-source_suffix>`_:
# The suffix of source filenames.
source_suffix = ".rst"

# **CodeChat note:** _`CodeChat_lexer_for_glob` is a dict of {glob_,
# lexer_alias}, which uses lexer_alias (e.g. a lexer's `short name
# <http://pygments.org/docs/lexers/>`_) to analyze any file which matches the
# given glob-style pattern (e.g. `glob
# <https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.match>`_.
CodeChat_lexer_for_glob = {
    # CSS files are auto-detected as a CSS + Lasso file by Pygments,
    # causing it to display incorrectly. Define them as CSS only.
    "*.css": "CSS",
    # These files use # as a comment. So does Perl. Ugly, no?
    ".gitignore": "Perl",
    "MANIFEST.in": "Perl",
    "docs-requirements.txt": "Perl",
    ".flake8": "Perl",
    # Treat JavaScript as plain JavaScript; the auto-detect code finds something else.
    "*.js": "JavaScript",
    # The ``codechat_config.json`` file is actually Python.
    "codechat_config.json": "Python",
}

# **CodeChat note:** _`CodeChat_excludes` is a list of exclude_patterns_ which
# applies only to source documents; in constrast, exclude_patterns_ will exclude
# the given files from all of Sphinx (for example, exclude_patterns_ files
# won't be included even if they're mentioned in html_static_path_).
CodeChat_excludes = ["CodeChat.css"]
# `source_encoding <http://sphinx-doc.org/config.html#confval-source_encoding>`_:
# The encoding of source files.
##source_encoding = 'utf-8-sig'

# `master_doc <http://sphinx-doc.org/config.html#confval-master_doc>`_: The
# master toctree document.
master_doc = "index"

# `language <http://sphinx-doc.org/config.html#confval-language>`_:
# The language for content autogenerated by Sphinx. Refer to documentation for a
# list of supported languages.
##language = None

# `exclude_patterns <http://sphinx-doc.org/config.html#confval-exclude_patterns>`_:
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
#
# **Important:** Do **NOT** add ``CodeChat.css`` to this list; this will
# instruct Sphinx not to copy it to the ``_static`` directory, where it
# is needed to properly lay out CodeChat output. Instead, to exclude it
# from the documents produced by Sphinx, add it to CodeChat_excludes_.
exclude_patterns = [
    # Misc files.
    "Thumbs.db",
    ".DS_Store",
    ".pytest_cache",
    "**/.mypy_cache",
    # **CodeChat notes:**
    #
    # By default, Enki will instruct Sphinx to place all Sphinx output in
    # ``_build``; this directory should therefore be excluded from the list of
    # source files.
    "_build",
    #
    # JavaScript/TypeScript generated files
    "VSCode_Extension/node_modules",
    "VSCode_Extension/out",
    "VSCode_Extension/.vscode",
    "**/gen-*",
    "**/gen_*",
    #
    # Files generated by packaging.
    "CodeChat_Server/build",
    "CodeChat_Server/dist",
    "**/*.egg-info",
    #
    # Libraries
    "CodeChat_Server/CodeChat_Server/CodeChat_Client/static/thrift.js",
    "CodeChat_Server/CodeChat_Server/CodeChat_Client/static/splitter*.*",
    "CodeChat_Server/CodeChat_Server/rst_templates",
    "CodeChat_Server/CodeChat_Server/rst_templates",
]


# `default_role <http://sphinx-doc.org/config.html#confval-default_role>`_: The
# reST default role (used for this markup: ```text```) to use for all documents.
default_role = "any"

# `keep_warnings <http://sphinx-doc.org/config.html#confval-keep_warnings>`_: If
# true, keep warnings as "system message" paragraphs in the built documents.
# Regardless of this setting, warnings are always written to the standard error
# stream when sphinx-build is run. **CodeChat note**: This should always be
# True; doing so places warnings next to the offending text in the web view,
# making them easy to find and fix.
keep_warnings = True
#
# `Options for HTML output <http://sphinx-doc.org/config.html#options-for-html-output>`_
# ======================================================================================
# `html_theme <http://sphinx-doc.org/config.html#confval-html_theme>`_: The
# theme to use for HTML and HTML Help pages.
html_theme = "alabaster"

# `html_theme_options <http://sphinx-doc.org/config.html#confval-html_theme_options>`_:
# Theme options are theme-specific and customize the look and feel of a theme
# further.
##html_theme_options = {}

# `html_style <http://sphinx-doc.org/config.html#confval-html_style>`_: The
# style sheet to use for HTML pages.
##html_style = None

# `html_theme_path <http://sphinx-doc.org/config.html#confval-html_theme_path>`_:
# Add any paths that contain custom themes here, relative to this directory.
##html_theme_path = []

# `html_title <http://sphinx-doc.org/config.html#confval-html_title>`_: The
# name for this set of Sphinx documents.  If None, it defaults to ``<project>
# v<release> documentation``.
##html_title = None

# `html_short_title <http://sphinx-doc.org/config.html#confval-html_short_title>`_:
# A shorter title for the navigation bar.  Default is the same as html_title.
##html_short_title = None

# `html_logo <http://sphinx-doc.org/config.html#confval-html_logo>`_: The name
# of an image file (relative to this directory) to place at the top of the
# sidebar.
##html_logo = None

# `html_favicon <http://sphinx-doc.org/config.html#confval-html_favicon>`_: The
# name of an image file (within the static path) to use as favicon of the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels
# large.
##html_favicon = None

# `html_static_path <http://sphinx-doc.org/config.html#confval-html_static_path>`_:
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files, so
# a file named ``default.css`` will overwrite the builtin ``default.css``.
# **CodeChat note:** Include the path to CodeChat's static files.
html_static_path = CodeChat.CodeToRest.html_static_path()

# `html_last_updated_fmt <http://sphinx-doc.org/config.html#confval-html_last_updated_fmt>`_:
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b, %d, %Y"

# `html_sidebars <http://sphinx-doc.org/config.html#confval-html_sidebars>`_:
# Custom sidebar templates, maps document names to template names.
##html_sidebars = {}

# `html_additional_pages <http://sphinx-doc.org/config.html#confval-html_additional_pages>`_:
# Additional templates that should be rendered to pages, maps page names to
# template names.
##html_additional_pages = {}

# `html_domain_indices <http://sphinx-doc.org/config.html#confval-html_domain_indices>`_:
# If false, no module index is generated.
##html_domain_indices = True

# `html_use_index <http://sphinx-doc.org/config.html#confval-html_use_index>`_:
# If false, no index is generated.
##html_use_index = True

# `html_split_index <http://sphinx-doc.org/config.html#confval-html_split_index>`_:
# If true, the index is split into individual pages for each letter.
##html_split_index = False

# `html_copy_source <http://sphinx-doc.org/config.html#confval-html_copy_source>`_:
# If true, the reST sources are included in the HTML build as _sources/name.
html_copy_source = True

# `html_show_sourcelink <http://sphinx-doc.org/config.html#confval-html_show_sourcelink>`_:
# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# `html_sourcelink_suffix <http://sphinx-doc.org/config.html#confval-html_sourcelink_suffix>`_:
# Suffix to be appended to source links (see html_show_sourcelink), unless they
# have this suffix already.
html_sourcelink_suffix = ""

# `html_show_sphinx <http://sphinx-doc.org/config.html#confval-html_show_sphinx>`_:
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
##html_show_sphinx = True

# `html_show_copyright <http://sphinx-doc.org/config.html#confval-html_show_copyright>`_:
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
##html_show_copyright = True

# `html_use_opensearch <http://sphinx-doc.org/config.html#confval-html_use_opensearch>`_:
# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
##html_use_opensearch = ''

# `html_file_suffix <http://sphinx-doc.org/config.html#confval-html_file_suffix>`_:
# This is the file name suffix for HTML files (e.g. ".xhtml").
##html_file_suffix = None
#
# Options for `Graphviz output <https://www.sphinx-doc.org/master/usage/extensions/graphviz.html>`_
# ===========================================================================================================
# The output format for Graphviz when building HTML files.
graphviz_output_format = "svg"
