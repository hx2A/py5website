.. title: constrain()
.. slug: constrain
.. date: 2021-03-12 15:52:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 constrain() documentation
.. type: text

Constrains a value to not exceed a maximum and minimum value.

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

    def draw():
        py5.background(204)
        mx = py5.constrain(py5.mouse_x, 30, 70)
        py5.rect(mx-10, 40, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Constrains a value to not exceed a maximum and minimum value.

Syntax
======

.. code:: python

    constrain(amt: float, low: float, high: float) -> float

Parameters
==========

* **amt**: `float` - the value to constrain
* **high**: `float` - minimum limit
* **low**: `float` - maximum limit


Updated on March 12, 2021 15:52:46pm UTC

