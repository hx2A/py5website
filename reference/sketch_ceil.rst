.. title: ceil()
.. slug: ceil
.. date: 2021-03-13 17:44:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 ceil() documentation
.. type: text

Calculates the closest int value that is greater than or equal to the value of the parameter.

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
        x = 2.88
        a = py5.ceil(x)  # Sets 'a' to 3

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the closest int value that is greater than or equal to the value of the parameter.

This function makes a call to the numpy ``ceil()`` function.

Syntax
======

.. code:: python

    ceil(value: float) -> int

Parameters
==========

* **value**: `float` - number to round up


Updated on March 13, 2021 17:44:45pm UTC

