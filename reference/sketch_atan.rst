.. title: atan()
.. slug: atan
.. date: 2021-03-09 14:45:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 atan() documentation
.. type: text

The inverse of :doc:`tan`, returns the arc tangent of a value.

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
        a = py5.PI/3
        t = py5.tan(a)
        a_t = py5.atan(t)
        # prints "1.04719757 : 1.73205087 : 1.04719757"
        print(round(a, 8), ':', round(t, 8), ':', round(a_t, 8))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = py5.PI + py5.PI/3
        t = py5.tan(a)
        a_t = py5.atan(t)
        # prints "4.18879027 : 1.73205106 : 1.04719761"
        print(round(a, 8), ':', round(t, 8), ':', round(a_t, 8))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The inverse of :doc:`tan`, returns the arc tangent of a value. This function expects the values in the range of -Infinity to Infinity and values are returned in the range ``-HALF_PI`` to ``HALF_PI``.

This function makes a call to the numpy ``atan()`` function.

Syntax
======

.. code:: python

    atan(value: float) -> float

Parameters
==========

* **value**: `float` - value whose arc tangent is to be returned


Updated on March 09, 2021 14:45:46pm UTC

