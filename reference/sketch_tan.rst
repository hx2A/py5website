.. title: tan()
.. slug: tan
.. date: 2021-03-09 14:45:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 tan() documentation
.. type: text

Calculates the ratio of the sine and cosine of an angle.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_tan_0.png
    :alt: example picture for tan()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = 0
        for i in range(50):
            py5.line(2*i, 50, 2*i, 50+2*py5.tan(a))
            a += py5.TWO_PI/50

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the ratio of the sine and cosine of an angle. This function expects the values of the angle parameter to be provided in radians (values from ``0`` to ``TWO_PI``). Values are returned in the range infinity to -infinity.

This function makes a call to the numpy ``tan()`` function.

Syntax
======

.. code:: python

    tan(angle: float) -> float

Parameters
==========

* **angle**: `float` - angle in radians


Updated on March 09, 2021 14:45:46pm UTC

