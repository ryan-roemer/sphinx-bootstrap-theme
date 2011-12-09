========================
 Sphinx Bootstrap Theme
========================

This repository integrates the Twitter Bootstrap_ CSS / JavaScript framework
as a Sphinx_ theme_. A live demo_ is available to preview the theme.

.. _Bootstrap: http://twitter.github.com/bootstrap/
.. _Sphinx: http://sphinx.pocoo.org/
.. _theme: http://sphinx.pocoo.org/theming.html
.. _demo: http://ryan-roemer.github.com/sphinx-bootstrap-theme


Installation
============
To install the theme, download the theme directory and update your
configuration

1. Create a "_themes" directory in your project source root.
2. Get the "bootstrap" themes either as raw files or as a zipfile from
   the repository.

   a. Most current way is to just clone this repo or download the full
      repo source and move the "bootstrap" directory to "_themes".
   b. Alternatively, there are some prepackaged theme zip files (containing
      only the theme files), which can be read directly by Sphinx. See the
      repo downloads_ page for available packages. Then download and rename
      to "bootstrap.zip"::

        $ cd /path/to/_themes
        $ wget https://github.com/downloads/ryan-roemer/sphinx-bootstrap-theme/bootstrap-3c64e4059b6b0fcae4253e7a410febc7aab3d9ca.zip
        $ mv bootstrap-*.zip bootstrap.zip

3. Edit your configuration file to point to the bootstrap theme::

      # Activate the theme.
      sys.path.append(os.path.abspath('_themes'))
      html_theme_path = ['_themes']
      html_theme = 'bootstrap'

      # Optional. Use a shorter name to conserve nav. bar space.
      html_short_title = "Demo"

.. _downloads: https://github.com/ryan-roemer/sphinx-bootstrap-theme/downloads

Theme Notes
===========
Sphinx
------
The theme places the global TOC, local TOC, navigation (prev, next) and
source links all in the top Bootstrap navigation bar, along with the Sphinx
search bar on the left side.

The global (site-wide) table of contents is the "Site" navigation dropdown,
which is a multi-level deep rendering of the ``toctree`` for the entire site.
The local (page-level) table of contents is the "Page" navigation dropdown,
which is a multi-level rendering of the current page's ``toc``.

Generally speaking, this is a quick and dirty hack to get the basic theme
going, so there are likely some oversights and lurking issues. Help and
bug filings for the project are most welcome.


Bootstrap
---------
The theme uses the following files from Twitter Bootstrap v1.4.0::

    bootstrap-dropdown.js
    bootstrap-scrollspy.js
    bootstrap.css

You can drop different versions in your Sphinx "_static" directory to
override these files.


Licenses
========
Sphinx Bootstrap Theme is licensed under the MIT_ license.

Twitter Bootstrap is licensed under the Apache_ license.

.. _MIT: https://github.com/ryan-roemer/sphinx-bootstrap-theme/blob/master/LICENSE.txt
.. _Apache: https://github.com/twitter/bootstrap/blob/master/LICENSE
