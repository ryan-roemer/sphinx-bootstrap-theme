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

Upgrade Notes
=============

When upgrading, you must upgrade **both** Bootstrap and Bootswatch --- Bootswatch
releases are custom tailored to the a specific version of Bootstrap.  The version of
jQuery (1.11) should be OK to leave as is unless a specific issue arises.

In the below examples we are upgrading to bootstrap 3.3.7; Bootstrap 2 versions should
not have a need to be changed.

Updating Bootstrap
------------------

1. Get new ``bootstrap-VERSION`` and drop in ``bootstrap/static``.

   - New versions should be available `here <http://getbootstrap.com/getting-started/#download>`_.
   - Choose "Bootstrap":

     ..

        Compiled and minified CSS, JavaScript, and fonts.  No docs or original
        source files are included.

2. Manually grep and replace instances of ``(jQuery)`` with
   ``(window.$jqTheme || window.jQuery)`` in files in the new
   ``bootstrap-VERSION/js`` directory.  See below.

3. Update ``VERSION`` in ``sphinx_bootstrap_theme/bootstrap/layout.html``:

   .. code-block:: jinja

      {% if theme_bootstrap_version == "3" %}
        {% set bootstrap_version, navbar_version = "3.3.7", "" %}
        {% set bs_span_prefix = "col-md-" %}
      {% else %}
        {% set bootstrap_version, navbar_version = "2.3.2", "-2" %}
        {% set bs_span_prefix = "span" %}
      {% endif %}

4. Update ``VERSION`` in ``sphinx_bootstrap_theme/bootstrap/static/bootstrap-sphinx.css_t``

   .. code-block:: jinja

      {% if theme_bootstrap_version == "3" %}
        {% set bootstrap_version, bootstrap_additional_css = "3.3.7", "theme" %}
      {% else %}
        {% set bootstrap_version, bootstrap_additional_css = "2.3.2", "responsive" %}
      {% endif %}

Choose your favorite text replacement tool for step 2, we will use ``grep`` and ``sed``.
The example here will be with the file ``bootstrap.js`` for understandability (since it
is not minified).

.. code-block:: console

   # First, locate the all of the calls to jQuery
   $ grep -Hn --color=auto '(jQuery)' bootstrap.js
   bootstrap.js:17:}(jQuery);
   bootstrap.js:77:}(jQuery);
   bootstrap.js:172:}(jQuery);
   bootstrap.js:298:}(jQuery);
   bootstrap.js:536:}(jQuery);
   bootstrap.js:749:}(jQuery);
   bootstrap.js:915:}(jQuery);
   bootstrap.js:1255:}(jQuery);
   bootstrap.js:1776:}(jQuery);
   bootstrap.js:1885:}(jQuery);
   bootstrap.js:2058:}(jQuery);
   bootstrap.js:2214:}(jQuery);
   bootstrap.js:2377:}(jQuery);

   # Make the replacement in-place while creating
   # a bootstrap.js.bak file (backup of the original)
   $ sed -i.bak 's/(jQuery)/(window.$jqTheme || window.jQuery)/g' bootstrap.js

   # Verify there are no more (jQuery) left, and search our replacement
   # for sanity checking (all the line numbers should match up)
   $ grep -Hn --color=auto '(jQuery)' bootstrap.js
   $ grep -Hn --color=auto '(window.$jqTheme || window.jQuery)' bootstrap.js
   bootstrap.js:17:}(window.$jqTheme || window.jQuery);
   bootstrap.js:77:}(window.$jqTheme || window.jQuery);
   bootstrap.js:172:}(window.$jqTheme || window.jQuery);
   bootstrap.js:298:}(window.$jqTheme || window.jQuery);
   bootstrap.js:536:}(window.$jqTheme || window.jQuery);
   bootstrap.js:749:}(window.$jqTheme || window.jQuery);
   bootstrap.js:915:}(window.$jqTheme || window.jQuery);
   bootstrap.js:1255:}(window.$jqTheme || window.jQuery);
   bootstrap.js:1776:}(window.$jqTheme || window.jQuery);
   bootstrap.js:1885:}(window.$jqTheme || window.jQuery);
   bootstrap.js:2058:}(window.$jqTheme || window.jQuery);
   bootstrap.js:2214:}(window.$jqTheme || window.jQuery);
   bootstrap.js:2377:}(window.$jqTheme || window.jQuery);

   # IMPORTANT! Check your work!  Most of these were all in either
   # comments or error strings (that we want to leave as is),
   # but line 7 below needs to be updated!
   #
   # So line 7 should be changed (by you) to be
   #
   #     if (typeof (window.$jqTheme || window.jQuery) === 'undefined') {
   $ grep -Hn --color=auto 'jQuery' bootstrap.js
   bootstrap.js:7:if (typeof jQuery === 'undefined') {
   bootstrap.js:8:  throw new Error('Bootstrap\'s JavaScript requires jQuery')
   bootstrap.js:15:    throw new Error('Bootstrap\'s JavaScript requires jQuery version 1.9.1 or higher, but lower than version 4')
   bootstrap.js:17:}(window.$jqTheme || window.jQuery);
   bootstrap.js:77:}(window.$jqTheme || window.jQuery);
   bootstrap.js:172:}(window.$jqTheme || window.jQuery);
   bootstrap.js:298:}(window.$jqTheme || window.jQuery);
   bootstrap.js:536:}(window.$jqTheme || window.jQuery);
   bootstrap.js:749:}(window.$jqTheme || window.jQuery);
   bootstrap.js:915:}(window.$jqTheme || window.jQuery);
   bootstrap.js:1255:}(window.$jqTheme || window.jQuery);
   bootstrap.js:1260: * Inspired by the original jQuery.tipsy by Jason Frame
   bootstrap.js:1624:    // Avoid using $.offset() on SVGs since it gives incorrect results in jQuery 3.
   bootstrap.js:1776:}(window.$jqTheme || window.jQuery);
   bootstrap.js:1885:}(window.$jqTheme || window.jQuery);
   bootstrap.js:2058:}(window.$jqTheme || window.jQuery);
   bootstrap.js:2076:    // jscs:disable requireDollarBeforejQueryAssignment
   bootstrap.js:2078:    // jscs:enable requireDollarBeforejQueryAssignment
   bootstrap.js:2214:}(window.$jqTheme || window.jQuery);
   bootstrap.js:2377:}(window.$jqTheme || window.jQuery);

   # If all went according to plan, delete the backup
   $ rm bootstrap.js.bak


Update Bootswatch
-----------------

In this example we will walk through how to create the necessary structure using version
3.3.7 of Bootswatch.  When updating in the future, replace ``3.3.7`` in the below with
the version of Bootswatch you are upgrading to.  **Make sure** that you are upgrading
to the **same** version as Bootstrap!

.. code-block:: bash

    # Go to a familiar working location, we choose ~/Desktop for this example
    $ cd ~/Desktop

    # Download the source code for bootswatch
    $ git clone https://github.com/thomaspark/bootswatch.git
    $ cd bootswatch

    # Checkout the tagged release (use `git tag -l` to see all options)
    $ git checkout v3.3.7

    # We need to package every "theme/bootstrap.min.css", as well as the
    # fonts directory.  In the below, we are using a clever hack to include
    # the fonts directory by echoing it first so `tar` at the end will know
    # to copy it.  We then want to find all bootstrap.min.css files, but
    # need to ignore three directories: "2", "custom", and "bower_components".
    #
    # NOTE: the `echo` and `find` commands **MUST** be (in the same parentheses)
    #
    # You should be able to copy-paste this _without_ the leading $
    $ (echo "./fonts" &&                            \
              find . -name "bootstrap.min.css"      \
                  -not -path "./2/*"                \
                  -not -path "./bower_components/*" \
                  -not -path "./custom/*")          | \
          xargs tar -cf ~/Desktop/bootswatch-flat-3.3.7.tar

    # Now that we've extracted the relevant files, add them to the
    # sphinx_bootstrap_theme repo
    $ cd /path/to/sphinx-bootstrap-theme/sphinx_bootstrap_theme/bootstrap/static

    # Make the directory relevant to your bootswatch version and enter it;
    # the archive we made is not self-contained
    $ mkdir bootswatch-3.3.7
    $ cd bootswatch-3.3.7

    # Extract the archive we just created here
    $ cat ~/Desktop/bootswatch-flat-3.3.7.tar | tar -x

    # Make sure the themes you were expecting, **AND** the fonts directory are here
    $ ls
