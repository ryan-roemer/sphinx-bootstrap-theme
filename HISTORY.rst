=========
 History
=========

Current
=======
* Preserve HTML inside literal code blocks. (`@tristanlins`_)

v0.3.2
======
* Fix scroll handlers for nav. bar. (`@sccolbert`_)
* Fix background color visibility behind rounding in code blocks. (`@kosiakk`_)

v0.3.1
======
* Re-add ``navbar_links`` theme option lost in bad merge. (`@newgene`_)
* Fixed display of sidebar. (`@adamcharnock`_, `@russell`_)

v0.3.0
======
* Add Bootstrap v3.0.0 with legacy option for v2.3.2. (`@MiCHiLU`_)

v0.2.9
======
* Add ``navbar_links`` theme option. (`@newgene`_)
* Add ``navbarextra`` block in "layout.html". (`@grncdr`_)

v0.2.8
======
* Sphinx compatible Sidebars. (`@russell`_)
* Topnav sidebarrel can now be disabled. (`@russell`_)
* Topnav page nav menu can now be disabled. (`@russell`_)

v0.2.7
======
* Add custom nav bar links. (`@russell`_)
  Completes `#34 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/34>`_.
* Fix wrapping of line numbers in code includes. (`@russell`_)
  Fixes `#35 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/35>`_.
* Truncate long page titles in navigation bar. (`@aababilov`_)
  Fixes `#27 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/27>`_.

v0.2.6
======
* Use network path for Bootswatch (`@nail`_)
* Switch from distribute to setuptools. (Suggested by `@thedrow`_)

v0.2.5
======
* Search page styling. (`@russell`_)

v0.2.4
======
* Adjust the max width of field lists. (`@russell`_)
* Update to Bootstrap v2.3.2.
* Navbar search box now uses bootstrap search-query class. (`@russell`_)
* Field-list tables now have an inherited width. (`@russell`_)

v0.2.3
======
* Put navbar within a `container`. (`@inducer`_)
* Add `navbar_site_name` for renaming site nav. tab. (Suggested by `@inducer`_)

v0.2.2
======
* Better literal markup handling for Bootstrap code formatting. (`@russell`_)
* Scroll window when jumping to an anchor. (`@russell`_)

v0.2.1
======
* Fix code styling collision for cross references and inline code blocks.
  (`@russell`_)

v0.2.0
======
* Update to Bootstrap v2.3.1.
* Add ``bootswatch_theme`` option for `Bootswatch <http://bootswatch.com>`_
  CSS theme support. (`@zyga`_)

v0.1.8
======
* Add ``globaltoc_includehidden`` option.

v0.1.7
======
* Add Python 3 support. (`@zyga`_)
* Add support for ``navbar_title`` theme configuration. The documentation
  originally stated that ``html_short_title`` was supported for overriding the
  navbar title (brand), but this never actually worked.
  (Thanks to Tim Kedmenec for pointing this out).

v0.1.4
======
* Remove the ``Site`` nav button if no other pages.
* Added jQuery v1.9.1 with ``noConflict()`` to allow underlying Sphinx to use
  whatever jQuery it wants.
* Update to Bootstrap v2.3.0.
* Fix multi-word Bootstrap-styled ``code`` elements.

v0.1.3
======
* Convert inline code to Bootstrap-styled ``code`` elements.

v0.1.2
======
* Add ``globaltoc_depth`` theme option.
* Add Bootstrap alert styling to "note", "warning" Sphinx directives.

v0.1.1
======
* Add Bootstrap table styling.

v0.1.0
======
* Add support for deployment via PyPI.

v0.0.6
======
* Fix logo display in navbar.

v0.0.4
======
* Get mobile (iPhone) viewport and nav menus working.
* Add new theme options ``navbar_class``, ``source_link_position``.

v0.0.3
======
* Update to Bootstrap v2.2.1.
* Switch to responsive CSS.
* Make navbar menus do real dropdowns recursively.

v0.0.2
======
* Update to Bootstrap v2.0. (`@oscarcp`_)

v0.0.1
======
* Original theme based on Bootstrap v1.4.0.

.. _@aababilov: https://github.com/aababilov
.. _@adamcharnock: https://github.com/adamcharnock
.. _@grncdr: https://github.com/grncdr
.. _@inducer: https://github.com/inducer
.. _@kosiakk: https://github.com/kosiakk
.. _@MiCHiLU: https://github.com/MiCHiLU
.. _@nail: https://github.com/nail
.. _@newgene: https://github.com/newgene
.. _@oscarcp: https://github.com/oscarcp
.. _@russell: https://github.com/russell
.. _@sccolbert: https://github.com/sccolbert
.. _@thedrow: https://github.com/thedrow
.. _@tristanlins: https://github.com/tristanlins
.. _@zyga: https://github.com/zyga
