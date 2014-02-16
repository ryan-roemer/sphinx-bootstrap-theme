# coding=utf-8
"""
Example Module to show of :py:mod:`sphinx.autodoc` features with **Twitter Bootstrap**.

.. moduleauthor:: Torbjörn Klatt <opensource@torbjoern-klatt.de>
"""


class ExampleClass(object):
    """
    Example Class

    An example class, which is documented.
    """

    def __init__(self):
        """
        Constructor

        Constructs an instance of :py:class:`.Example`.
        """
        self._private_variable = None

    def hello(self, greeting='Hello', name='world'):
        """
        Prints a welcome message

        :param str greeting: Greeting text.
            A second line.

            And second paragraph.
        :param str name: Name to greet.
        :returns: nothing
        :raises ValueError: if ``name`` is not a string or empty
        """
        if isinstance(name, str) and str != '':
            print('%s %s!!' % (greeting, name))
        else:
            raise ValueError("Name must not be empty.")


__all__ = ['ExampleClass']
