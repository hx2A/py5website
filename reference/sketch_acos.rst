.. title: acos()
.. slug: acos
.. date: 2021-03-09 14:45:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 acos() documentation
.. type: text

The inverse of :doc:`cos`, returns the arc cosine of a value.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = py5.PI
        c = py5.cos(a)
        a_c = py5.acos(c)
        # prints "3.1415927 : -1.0 : 3.14159261"
        print(round(a, 8), ':', round(c, 8), ':', round(a_c, 8))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = py5.PI + py5.PI/4
        c = py5.cos(a)
        a_c = py5.acos(c)
        # prints "3.92699087 : -0.70710674 : 2.35619443"
        print(round(a, 8), ':', round(c, 8), ':', round(a_c, 8))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The inverse of :doc:`cos`, returns the arc cosine of a value. This function expects the values in the range of -1 to 1 and values are returned in the range ``0`` to ``PI``.

This function makes a call to the numpy ``acos()`` function.

Syntax
======

.. code:: python

    acos(value: float) -> float

Parameters
==========

* **value**: `float` - value in the range of -1 to 1 whose arc cosine is to be returned


Updated on March 09, 2021 14:45:46pm UTC

