==========
 Examples
==========

Various examples of Bootstrap styling applied to Sphinx constructs. You can
view the `source <./_sources/examples.txt>`_ of this page to see the specific
reStructuredText used to create these examples.

Headings
========
This is a first level heading (``h1``).

Sub-Heading
-----------
This is a second level heading (``h2``).

Sub-Sub-Heading
~~~~~~~~~~~~~~~
This is a third level heading (``h3``).


Code
====
The Sphinx Bootstrap Theme uses Bootstrap styling for ``inline code text`` and
::

    multiline
    code text

Here's an included example with line numbers.

.. literalinclude:: ../../sphinx_bootstrap_theme/__init__.py
   :linenos:

It also works with existing Sphinx highlighting:

.. code-block:: html

    <html>
      <body>Hello World</body>
    </html>

.. code-block:: python

    def hello():
        """Greet."""
        return "Hello World"

.. code-block:: javascript

    /**
     * Greet.
     */
    function hello(): {
      return "Hello World";
    }


Admonitions
===========
The Sphinx Bootstrap Theme uses the Bootstrap ``alert`` classes for Sphinx
admonitions.

Note
----
.. note:: This is a note.

Warning
-------
.. warning:: This is a warning.


.. TODO
  Footnotes
  =========
  I have footnoted a first item [#f1]_ and second item [#f2]_.

  .. rubric:: Footnotes
  .. [#f1] My first footnote.
  .. [#f2] My second footnote.

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

which uses the directive::

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

which uses the directive::

    .. cssclass:: table-striped

And a "**hoverable**" table:

.. cssclass:: table-hover

=====  =====  =======
H1     H2     H3
=====  =====  =======
cell1  cell2  cell3
...    ...    ...
...    ...    ...
=====  =====  =======

which uses the directive::

    .. cssclass:: table-hover

Code Documentation
==================

An example Python function.

.. py:function:: format_exception(etype, value, tb[, limit=None])

   Format the exception with a traceback.

   :param etype: exception type
   :param value: exception value
   :param tb: traceback object
   :param limit: maximum number of stack frames to show
   :type limit: integer or None
   :rtype: list of strings

An example JavaScript function.

.. js:class:: MyAnimal(name[, age])

   :param string name: The name of the animal
   :param number age: an optional age for the animal
