"""
Example docstring 1

* A thing.
* Another thing.

or

1. Item 1.
2. Item 2.
3. Item 3.

or

- Some.
- Thing.
- Different.

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

SIMPLE TABLE:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

`Docs for this project <http://packages.python.org/an_example_pypi_project/>`_

This is a statement.

.. warning::

   Never, ever, use this code!

.. versionadded:: 0.0.1

It's okay to use this code.

"""


import antigravity


def foo(a, b):
    """Does a thing.

    :param a: 1
    :param b: the word 'three'
    :returns: 1
    :rtype: int

    """
    return 1


class bar(object):
    """ Doesn't do anything
    """
    def __init__(self, baz):
        """Init example.

        :param baz: Whatever, man.
        :returns: None
        :rtype: None

        """
        pass
    a = 1
