=========
 History
=========

v0.6.4
======
* Fix ``setup()`` function. (`@karelv`_)
  `#176 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/176>`_.

v0.6.3
======
* Declare supported Python versions. (`@troeger`_)
  `#175 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/175>`_.

v0.6.2
======
* Add theme ``setup()`` function. (`@karelv`_)
  `#172 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/172>`_.

v0.6.1
======
* Fix headerlink margin. (`@timhoffm`_)
  `#170 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/170>`_.

v0.6.0
======
* Upgrade to Bootstrap / Bootswatch v3.3.7. (`@svenevs`_)
  `#164 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/164>`_.

v0.5.3
======
* Fix sidebar jQuery issue with height. (`@Sheile`_)
  `#157 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/157>`_.

v0.5.2
======
*bad release*

v0.5.1
======
* Fix ``@import url()`` CSS imports to be relative paths so that you can have a
  non-root / nested site.

v0.5.0
======
* Fix ``css_files`` breakage from Sphinx ``1.6+`` update.
  `#158 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/158>`_,
  `#160 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/160>`_.

* **Breaking Change**: Remove ``bootswatch_css_custom`` override, and instead opt for documenting idiomatic Sphinx-version specific generic overrides for custom CSS.

v0.4.14
=======
* Fix visibiliy of multiple footnote references. (`@drewhutchison`_)
  `#152 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/152>`_.

v0.4.13
=======
* Fix search with larger sidebar. (`@cemsbr`_)
  `#148 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/148>`_.

v0.4.12
=======
* Fix typo in theme CSS rule. (`@vkoby`_)
  `#144 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/144>`_.

v0.4.11
=======
* Fix logo sizing issue on mobile with RTD.
  `#142 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/142>`_.


v0.4.10
=======
* Fix logo / brand title wrapping bug. (`@miketheman`_)
  `#141 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/141>`_.

v0.4.9
======
* Update to Bootstrap v3.3.6 and Bootswatch v3.3.6+1. (`@ppyv`_)

v0.4.8
======
* Fix sidenav overflow / scrolling.
  `#136 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/136>`_.

v0.4.7
======
* Fix jumpy sidenav
  `#131 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/pull/131>`_.
  (`@cslarsen`_)

v0.4.6
======
* Switch demo to "sandstone" theme.
* Update to Bootswatch v3.3.4+1.
* Update to Bootstrap v3.3.4.
* Update Sphinx website links. (`@mrmsl`_)

v0.4.5
======
* Add Glyphicon fonts to Bootswatch 2 static assets. Also add example using the
  icons so we can catch errors like this better in the future.
* Fix CSS generation with ``'navbar_fixed_top': "false"`` and
  ``'bootstrap_version': "2"``.
  Fixes `#121 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/121>`_.
  (`@EricFromCanada`_)

v0.4.4
======
* Reset ``.container`` padding after Sphinx 1.3b commit overrode CSS.
  Fixes `#114 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/114>`_.
  (`@EricFromCanada`_)
* Fix situation where Python 3 + modern Sphinx results in empty strings being
  interpreted as a non-existent Bootswatch theme for
  ``theme_bootswatch_theme`` by permissively allowing old (empty quotes) or
  new (empty or ``None``) styles.
  Fixes `#115 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/115>`_.
  (`@EricFromCanada`_, `@peteut`_, `@mdboom`_)

v0.4.3
======
* Add ``fonts/`` directories to bootswatch. (`@gkthiruvathukal`_)
* Remove divider-vertical from BS3 navbar.html. (`@kaycebasques`_)

v0.4.2
======
* Update to Bootstrap v3.2.0.

v0.4.1
======
* Fix non-fixed-top navbar. (`@Danack`_)
* Add config option for page name tab. (`@masklinn`_)

v0.4.0
======
* Fix bug preventing Glyphicons from working with Bootswatch themes.

v0.3.9
======
* Restyle alerts and admonitions. (`@masklinn`_)

v0.3.8
======
* Update to Bootstrap v3.1.0. (`@torbjoernk`_)

v0.3.7
======
* Add footnote styling. (`@russell`_)
* Update search.html to allow search locally. (`@fjfeijoo`_)
* Updated search template for BS3. (`@russell`_)

v0.3.6
======
* Add bootswatch glyphicon links in bootswatch.
* Selectively hide links on navbar in certain view sizes. From here on out,
  `hidden-sm` in BS3 is applied to next/previous and source navigation links.
* Make navbar logo work with subdirectories. (`@cdbennett`_)

v0.3.5
======
* Adds navbar logo's back to BS3. Switch to actual ``<img>`` tags for logos.
  Fixes `#52 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/52>`_.
* Fix responsive Bootswatch for Bootstrap v2.

v0.3.4
======
* Switch demo to "flatly" theme.
* Fix the long-broken "Source" nav. link.
* Add missing "flatly" to bootswatch CSS static files.

v0.3.3
======
* Allow custom CSS overrides, even on Bootstrap CSS.
  Completes `#68 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/68>`_.
* Add offline bootswatch files.
  Completes `#19 <https://github.com/ryan-roemer/sphinx-bootstrap-theme/issues/19>`_.
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
.. _@cdbennett: https://github.com/cdbennett
.. _@cemsbr: https://github.com/cemsbr
.. _@cslarsen: https://github.com/cslarsen
.. _@Danack: https://github.com/Danack
.. _@drewhutchison: https://github.com/drewhutchison
.. _@EricFromCanada: https://github.com/EricFromCanada
.. _@fjfeijoo: https://github.com/fjfeijoo
.. _@gkthiruvathukal: https://github.com/gkthiruvathukal
.. _@grncdr: https://github.com/grncdr
.. _@inducer: https://github.com/inducer
.. _@karelv: https://github.com/karelv
.. _@kaycebasques: https://github.com/kaycebasques
.. _@kosiakk: https://github.com/kosiakk
.. _@masklinn: https://github.com/masklinn
.. _@mdboom: https://github.com/mdboom
.. _@MiCHiLU: https://github.com/MiCHiLU
.. _@miketheman: https://github.com/miketheman
.. _@mrmsl: https://github.com/mrmsl
.. _@nail: https://github.com/nail
.. _@newgene: https://github.com/newgene
.. _@oscarcp: https://github.com/oscarcp
.. _@peteut: https://github.com/peteut
.. _@ppyv: https://github.com/ppyv
.. _@russell: https://github.com/russell
.. _@sccolbert: https://github.com/sccolbert
.. _@Sheile: https://github.com/Sheile
.. _@shiumachi: https://github.com/shiumachi
.. _@svenevs: https://github.com/svenevs
.. _@thedrow: https://github.com/thedrow
.. _@timhoffm: https://github.com/timhoffm
.. _@torbjoernk: https://github.com/torbjoernk
.. _@tristanlins: https://github.com/tristanlins
.. _@troeger: https://github.com/troeger
.. _@vkoby: https://github.com/vkoby
.. _@zyga: https://github.com/zyga
