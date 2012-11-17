========================
 Sphinx Bootstrap Theme
========================

This repository integrates the Twitter Bootstrap_ CSS / JavaScript framework
as a Sphinx_ theme_.

.. _Bootstrap: http://twitter.github.com/bootstrap/
.. _Sphinx: http://sphinx.pocoo.org/
.. _theme: http://sphinx.pocoo.org/theming.html


Demos
=====
Here is the theme in use for some of my public projects:

* `Sphinx Bootstrap Theme`_: This project, with a dark top navbar, using
  the theme option ``'navbar_class': "navbar navbar-inverse",``.
* `Django Cloud Browser`_: A Django reusable app for browsering cloud
  (e.g., Amazon Web Services S3) datastores.

.. _Sphinx Bootstrap Theme: http://ryan-roemer.github.com/sphinx-bootstrap-theme
.. _Django Cloud Browser: http://ryan-roemer.github.com/django-cloud-browser


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
      repo downloads_ page for available packages. Then download
      "bootstrap.zip"::

        $ cd /path/to/_themes
        $ wget https://github.com/downloads/ryan-roemer/sphinx-bootstrap-theme/bootstrap.zip

      In addition to the "current" release, the GitHub zipfiles have either git
      hash releases (for development builds) or tags for official tagged
      releases. E.g.::

        bootstrap.zip
        bootstrap-v0.0.4.zip
        bootstrap-f51d73491e9bae68eb1b1c57059d9e0ece03d125.zip

3. Edit the "conf.py" configuration file to point to the bootstrap theme::

      # Activate the theme.
      sys.path.append(os.path.abspath('_themes'))
      html_theme_path = ['_themes']
      html_theme = 'bootstrap'

.. _downloads: https://github.com/ryan-roemer/sphinx-bootstrap-theme/downloads


Customization
=============
The theme can be further customized with the following options by editing
the "conf.py" configuration::

    # (Optional) Use a shorter name to conserve nav. bar space.
    html_short_title = "Demo"

    # (Optional) Logo. Should be exactly 32x32 px to fit the nav. bar.
    # Path should be relative to the html_static_path setting (e.g.,
    # "_static") in source.
    html_logo = "my_logo.png"

    # Theme options are theme-specific and customize the look and feel of a
    # theme further.
    html_theme_options = {
        # HTML navbar class (Default: "navbar") to attach to <div> element.
        # For black navbar, do "navbar navbar-inverse"
        'navbar_class': "navbar navbar-inverse",


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
which is a multi-level deep rendering of the ``toctree`` for the entire site.
The local (page-level) table of contents is the "Page" navigation dropdown,
which is a multi-level rendering of the current page's ``toc``.

Generally speaking, this is a quick and dirty hack to get the basic theme
going, so there are likely some oversights and lurking issues. Help and
bug filings for the project are most welcome.


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
