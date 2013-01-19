========================
 Sphinx Bootstrap Theme
========================

This Sphinx_ theme_ integrates the Twitter Bootstrap_ CSS / JavaScript
framework with various layout options, hierarchical menu navigation,
and mobile-friendly responsive design.

.. _Bootstrap: http://twitter.github.com/bootstrap/
.. _Sphinx: http://sphinx.pocoo.org/
.. _theme: http://sphinx.pocoo.org/theming.html
.. _PyPI: http://pypi.python.org/pypi/sphinx-bootstrap-theme/
.. _GitHub repository: https://github.com/ryan-roemer/sphinx-bootstrap-theme


Introduction and Demos
======================
The theme is introduced and discussed in two blog posts:

* 12/09/2011 - `Twitter Bootstrap Theme for Sphinx <http://loose-bits.com/2011/12/09/sphinx-twitter-bootstrap-theme.html>`_
* 11/19/2012 - `Sphinx Bootstrap Theme Updates - Mobile, Dropdowns, and More <http://loose-bits.com/2012/11/19/sphinx-bootstrap-theme-updates.html>`_

Here is the theme in use for some of my public projects:

* `Sphinx Bootstrap Theme`_: This project, with a dark top navbar, using
  the theme option ``'navbar_class': "navbar navbar-inverse"``.
* `Django Cloud Browser`_: A Django reusable app for browsing cloud
  datastores (e.g., Amazon Web Services S3).

The theme demo website also includes an `examples page`_ for some useful
illustrations of getting Sphinx to play nicely with Bootstrap (also take a
look at the `examples source`_ for the underlying reStructuredText).

.. _Sphinx Bootstrap Theme: http://ryan-roemer.github.com/sphinx-bootstrap-theme
.. _examples page: http://ryan-roemer.github.com/sphinx-bootstrap-theme/examples.html
.. _examples source: http://ryan-roemer.github.com/sphinx-bootstrap-theme/_sources/examples.txt
.. _Django Cloud Browser: http://ryan-roemer.github.com/django-cloud-browser


Installation
============
Installation from PyPI_ is fairly straightforward:

1. Install the package::

      $ pip install sphinx_bootstrap_theme

2. Edit the "conf.py" configuration file to point to the bootstrap theme::

      # At the top.
      import sphinx_bootstrap_theme

      # ...

      # Activate the theme.
      html_theme = 'bootstrap'
      html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

..
  The theme can be installed from PyPI_ or downloaded as a zip file from
  GitHub.

  Install Python Package from PyPI
  --------------------------------

  Download Zip Bundle
  -------------------
  To install the theme from a bundled zip file, download the theme
  bundle from the theme website and update your configuration:

  1. Create a "_themes" directory in your project source root.
  2. Get the "bootstrap" theme either as raw files or as a zipfile.

     a. Most current way is to just clone this repo or download the full
        repo source and move the "bootstrap" directory to "_themes".
     b. Alternatively, there are some prepackaged theme zip files (containing
        only the theme files), which can be read directly by Sphinx. See the
        downloads_ page for available packages. Then download
        "bootstrap.zip"::

          $ cd /path/to/_themes
          $ wget https://github.com/ryan-roemer/sphinx-bootstrap-theme/_static/downloads/bootstrap.zip

  3. Edit the "conf.py" configuration file to point to the bootstrap theme::

        # Activate the theme.
        sys.path.append(os.path.abspath('_themes'))
        html_theme = 'bootstrap'
        html_theme_path = ['_themes']

  .. _downloads: http://ryan-roemer.github.com/sphinx-bootstrap-theme/downloads.html


Customization
=============
The theme can be further customized with the following options by editing
the "conf.py" configuration::

    # (Optional) Use a shorter name to conserve nav. bar space.
    html_short_title = "Demo"

    # (Optional) Logo. Should be exactly 24x24 px to fit the nav. bar.
    # Path should be relative to the static files directory.
    html_logo = "my_logo.png"

    # Theme options are theme-specific and customize the look and feel of a
    # theme further.
    html_theme_options = {
        # Global TOC depth for "site" navbar tab. (Default: 1)
        # Switching to -1 shows all levels.
        'globaltoc_depth': 2,

        # HTML navbar class (Default: "navbar") to attach to <div> element.
        # For black navbar, do "navbar navbar-inverse"
        'navbar_class': "navbar navbar-inverse",

        # Fix navigation bar to top of page?
        # Values: "true" (default) or "false"
        'navbar_fixed_top': "true",

        # Location of link to source.
        # Options are "nav" (default), "footer" or anything else to exclude.
        'source_link_position': "nav",
    }

Theme Notes
===========
Sphinx
------
The theme places the global TOC, local TOC, navigation (prev, next) and
source links all in the top Bootstrap navigation bar, along with the Sphinx
search bar on the left side.

The global (site-wide) table of contents is the "Site" navigation dropdown,
which is a configurable level rendering of the ``toctree`` for the entire site.
The local (page-level) table of contents is the "Page" navigation dropdown,
which is a multi-level rendering of the current page's ``toc``.


Bootstrap
---------
The theme uses Twitter Bootstrap v2.2.1. You can override any static JS/CSS
files by dropping different versions in your Sphinx "_static" directory.


Licenses
========
Sphinx Bootstrap Theme is licensed under the MIT_ license.

Twitter Bootstrap is licensed under the Apache_ license.

.. _MIT: https://github.com/ryan-roemer/sphinx-bootstrap-theme/blob/master/LICENSE.txt
.. _Apache: https://github.com/twitter/bootstrap/blob/master/LICENSE
