=========
 History
=========

v0.2.7
======

* Truncate long page titles in navigation bar (`@aababilov`_)

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

.. _@nail: https://github.com/nail
.. _@thedrow: https://github.com/thedrow
.. _@inducer: https://github.com/inducer
.. _@russell: https://github.com/russell
.. _@zyga: https://github.com/zyga
.. _@oscarcp: https://github.com/oscarcp
