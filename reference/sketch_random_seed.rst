.. title: random_seed()
.. slug: random_seed
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 random_seed() documentation
.. type: text

Sets the seed value for py5's random functions.

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
        py5.random_seed(42)
        a = py5.random()
        py5.random_seed(42)
        b = py5.random()
        # the values a and b will be the same
        py5.println(a, b)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.random_seed(0)
        for i in range(100):
            r = py5.random(255)
            py5.stroke(r)
            py5.line(i, 0, i, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the seed value for py5's random functions. This includes :doc:`random`, :doc:`random_int`, :doc:`random_choice`, and :doc:`random_gaussian`. By default, all of these functions would produce different results each time a program is run. Set the seed parameter to a constant value to return the same pseudo-random numbers each time the software is run.

Syntax
======

.. code:: python

    random_seed(seed: int) -> None

Parameters
==========

* **seed**: `int` - seed value


Updated on July 06, 2021 22:46:12pm UTC

