==========
 Examples
==========

Various examples of Bootstrap styling applied to Sphinx constructs.

Tables
======
Here are some examples of Sphinx
`tables <http://sphinx-doc.org/rest.html#rst-tables>`_. The Sphinx Bootstrap
Theme removes all Sphinx ``docutils`` classes and replaces them with the
default Bootstrap ``table`` class.  You can add additional table classes
using the Sphinx ``cssclass::`` directive, as demonstrated in the following
tables.

Grid
----
A "**bordered**" grid table:

.. cssclass:: table-bordered

+------------------------+------------+----------+----------+
| Header1                | Header2    | Header3  | Header4  |
+========================+============+==========+==========+
| row1, cell1            | cell2      | cell3    | cell4    |
+------------------------+------------+----------+----------+
| row2 ...               | ...        | ...      |          |
+------------------------+------------+----------+----------+
| ...                    | ...        | ...      |          |
+------------------------+------------+----------+----------+

which uses directive::

    .. cssclass:: table-bordered

Simple
------
A simple "**striped**" table:

.. cssclass:: table-striped

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======

which uses directive::

    .. cssclass:: table-striped

|
And a "**hoverable**" table:

.. cssclass:: table-hover

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======

which uses directive::

    .. cssclass:: table-hover
