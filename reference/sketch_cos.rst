.. title: cos()
.. slug: cos
.. date: 2021-03-09 14:45:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 cos() documentation
.. type: text

Calculates the cosine of an angle.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_cos_0.png
    :alt: example picture for cos()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        a = 0
        for i in range(25):
            py5.line(4*i, 50, 4*i, 50+40*py5.cos(a))
            a += py5.TWO_PI/25

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the cosine of an angle. This function expects the values of the angle parameter to be provided in radians (values from ``0`` to ``TWO_PI``). Values are returned in the range -1 to 1.

This function makes a call to the numpy ``cos()`` function.

Syntax
======

.. code:: python

    cos(angle: float) -> float

Parameters
==========

* **angle**: `float` - angle in radians


Updated on March 09, 2021 14:45:46pm UTC

