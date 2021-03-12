.. title: sqrt()
.. slug: sqrt
.. date: 2021-03-12 16:24:15 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 sqrt() documentation
.. type: text

Calculates the square root of a number.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_sqrt_0.png
    :alt: example picture for sqrt()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        a = py5.sqrt(6561)  # Sets 'a' to 81
        b = py5.sqrt(625)   # Sets 'b' to 25
        c = py5.sqrt(1)     # Sets 'c' to 1
        py5.rect(0, 25, a, 10)
        py5.rect(0, 45, b, 10)
        py5.rect(0, 65, c, 10)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_sqrt_1.png
    :alt: example picture for sqrt()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        a = py5.sqrt(6561)  # Sets 'a' to 81
        b = py5.sqrt(-625)   # Sets 'b' to the complex number (0+25j)

        if isinstance(a, complex):
            py5.fill(255, 0, 0)
            py5.rect(0, 25, a.imag, 10)
        else:
            py5.fill(255)
            py5.rect(0, 25, a, 10)

        if isinstance(b, complex):
            py5.fill(255, 0, 0)
            py5.rect(0, 45, b.imag, 10)
        else:
            py5.fill(255)
            py5.rect(0, 45, b, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the square root of a number. The square root of a positive number is always positive, even though there may be a valid negative root. The square root of a negative number is a complex number. In either case, the square root ``s`` of number ``a`` is such that ``s*s = a``. It is the opposite of squaring.

Python supports complex numbers, but such values cannot be passed to py5 drawing functions. When using the ``sqrt()`` function, you should check if the result is complex before using the value. You can also extract the real and imaginary components of the complex value with ``.real`` and ``.imag``. See the second example to learn how to do both of these things.

Syntax
======

.. code:: python

    sqrt(value: float) -> Union[float, complex]

Parameters
==========

* **value**: `float` - value to calculate the square root of


Updated on March 12, 2021 16:24:15pm UTC

