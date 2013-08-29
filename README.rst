========================
 Sphinx Bootstrap Theme
========================

This Sphinx_ theme_ integrates the Twitter Bootstrap_ CSS / JavaScript
framework with various layout options, hierarchical menu navigation,
and mobile-friendly responsive design. It is configurable, extensible
and can use any number of different Bootswatch_ CSS themes.

.. _Bootstrap: http://twitter.github.com/bootstrap/
.. _Sphinx: http://sphinx.pocoo.org/
.. _theme: http://sphinx.pocoo.org/theming.html
.. _PyPI: http://pypi.python.org/pypi/sphinx-bootstrap-theme/
.. _GitHub repository: https://github.com/ryan-roemer/sphinx-bootstrap-theme


Introduction and Demos
======================
The theme is introduced and discussed in the following posts:

* 12/09/2011 - `Twitter Bootstrap Theme for Sphinx <http://loose-bits.com/2011/12/09/sphinx-twitter-bootstrap-theme.html>`_
* 11/19/2012 - `Sphinx Bootstrap Theme Updates - Mobile, Dropdowns, and More <http://loose-bits.com/2012/11/19/sphinx-bootstrap-theme-updates.html>`_
* 2/12/2013 - `Sphinx Bootstrap Theme 0.1.6 - Bootstrap and Other Updates <http://loose-bits.com/2013/02/12/sphinx-bootstrap-theme-updates.html>`_
* 4/10/2013 - `Sphinx Bootstrap Theme 0.2.0 - Now with Bootswatch! <http://loose-bits.com/2013/04/10/sphinx-bootstrap-theme-bootswatch.html>`_

Examples of the theme in use for some public projects:

* `Sphinx Bootstrap Theme`_: This project, with the theme option
  ``'bootswatch_theme': "united"`` to use the "United_" Bootswatch_ theme.
* `Django Cloud Browser`_: A Django reusable app for browsing cloud
  datastores (e.g., Amazon Web Services S3).

The theme demo website also includes an `examples page`_ for some useful
illustrations of getting Sphinx to play nicely with Bootstrap (also take a
look at the `examples source`_ for the underlying reStructuredText).

.. _Bootswatch: http://bootswatch.com
.. _United: http://bootswatch.com/united
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


Customization
=============
The can be customized in varying ways (some a little more work than others).

Theme Options
-------------
The theme provides many built-in options that can be configured by editing
your "conf.py" file::

    # (Optional) Logo. Should be exactly 24x24 px to fit the nav. bar.
    # Path should be relative to the static files directory.
    html_logo = "my_logo.png"

    # Theme options are theme-specific and customize the look and feel of a
    # theme further.
    html_theme_options = {
        # Navigation bar title. (Default: ``project`` value)
        'navbar_title': "Demo",

        # Tab name for entire site. (Default: "Site")
        'navbar_site_name': "Site",

        # A list of tuples containting pages to link to.  The value should
        # be in the form [(name, page), ..]
        'navbar_links': [('Examples', 'examples')],

        # Render the next and previous page links in navbar. (Default: true)
        'navbar_sidebarrel': True,

        # Render the current pages TOC in the navbar. (Default: true)
        'navbar_pagenav': True,

        # Global TOC depth for "site" navbar tab. (Default: 1)
        # Switching to -1 shows all levels.
        'globaltoc_depth': 2,

        # Include hidden TOCs in Site navbar?
        #
        # Note: If this is "false", you cannot have mixed ``:hidden:`` and
        # non-hidden ``toctree`` directives in the same page, or else the build
        # will break.
        #
        # Values: "true" (default) or "false"
        'globaltoc_includehidden': "true",

        # HTML navbar class (Default: "navbar") to attach to <div> element.
        # For black navbar, do "navbar navbar-inverse"
        'navbar_class': "navbar navbar-inverse",

        # Fix navigation bar to top of page?
        # Values: "true" (default) or "false"
        'navbar_fixed_top': "true",

        # Location of link to source.
        # Options are "nav" (default), "footer" or anything else to exclude.
        'source_link_position': "nav",

        # Bootswatch (http://bootswatch.com/) theme.
        #
        # Options are nothing with "" (default) or the name of a valid theme
        # such as "amelia" or "cosmo".
        #
        # Note that this is served off CDN, so won't be available offline.
        'bootswatch_theme': "united",
    }

Note for the navigation bar title that if you don't specify a theme option of
``navbar_title`` that the "conf.py" ``project`` string will be used. We don't
use the ``html_title`` or ``html_short_title`` values because by default those
both contain version strings, which the navigation bar treats differently.

Bootswatch
----------
The theme option ``bootswatch_theme`` integrates (the totally awesome)
Bootswatch_ library, so you can choose between the various themes. The
themes, however, are served off a CDN, not from static files, which means that
if you are offline, you will see "normal", un-themed Bootstrap for your
documentation.

This seemed like the best compromise between the size issues with statically
including all of the various Bootswatch_ themes and actually making them
available online.

Extending "layout.html"
-----------------------
As a more "hands on" approach to customization, you can override any template
in this Sphinx theme or any others. A good candidate for changes is
"layout.html", which provides most of the look and feel. First, take a look
at the "layout.html" file that the theme provides, and figure out
what you need to override.

Then, create your own "_templates" directory and "layout.html" file (assuming
you build from a "source" directory)::

    $ mkdir source/_templates
    $ touch source/_templates/layout.html

Then, configure your "conf.py"::

    templates_path = ['_templates']

Finally, edit your override file "source/_templates/layout.html"::

    {# Import the theme's layout. #}
    {% extends "!layout.html" %}

    {# Add some extra stuff before and use exiting with 'super()' call. #}
    {% block footer %}
      <h2>My footer of awesomeness.</h2>
      {{ super() }}
    {% endblock %}


Adding Custom CSS
-----------------
Alternately, you could add your own custom static media directory with a CSS
file to override a style, which in the demo would be something like::

    $ mkdir source/_static
    $ touch source/_static/my-styles.css

Then, in "conf.py", edit this line::

    html_static_path = ["_static"]

You will also need the override template "source/_templates/layout.html" file
configured as above, but with the following code::

    {# Import the theme's layout. #}
    {% extends "!layout.html" %}

    {# Include our new CSS file into existing ones. #}
    {% set css_files = css_files + ['_static/my-styles.css']%}

Then, in the new file "source/_static/my-styles.css", add any appropriate
styling, e.g. a bold background color::

    footer {
      background-color: red;
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
The theme uses Twitter Bootstrap v2.3.1 and jQuery v.1.9.1. As the jQuery that
Bootstrap wants can radically depart from the jQuery Sphinx internal libraries
use, the library from this theme is integrated via ``noConflict()`` as
``$jqTheme``.

You can override any static JS/CSS files by dropping different versions in your
Sphinx "_static" directory.


Contributing
============
Contributions to this project are most welcome. Please make sure that the demo
site builds cleanly, and looks like what you want. First build the demo::

    $ fab clean && fab demo

Then, view the site in the development server::

    $ fab demo_server

Also, if you are adding a new type of styling or Sphinx or Bootstrap construct,
please add a usage example to the "Examples" page.


Licenses
========
Sphinx Bootstrap Theme is licensed under the MIT_ license.

Twitter Bootstrap is licensed under the Apache_ license.

.. _MIT: https://github.com/ryan-roemer/sphinx-bootstrap-theme/blob/master/LICENSE.txt
.. _Apache: https://github.com/twitter/bootstrap/blob/master/LICENSE
