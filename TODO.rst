=============
 Future Work
=============

CSS / Layout
============
* Search Bar: Is aligned right inconsistently in BS2 vs. BS3.
* Footnotes: Need much better styling. Maybe switch to tooltips.
* Optionally move the ``localtoc`` from the top navigation bar into it's own
  navbar below the page title.

Infrastructure
==============
* Re-enable the downloads.

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

Notes
=====

Updating bootswatch:

.. code-block:: bash

    $ cd scm/vendor/bootswatch
    $ find . -name "bootstrap.min.css" | \
      egrep -v "\/2|bower_components\/" | \
      xargs tar cf - > ~/Desktop/bootswatch-3.2.0.tar
    # TODO: AND... add the fonts too!
