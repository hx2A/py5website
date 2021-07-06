.. title: log()
.. slug: log
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 log() documentation
.. type: text

Calculates the natural logarithm (the base-e logarithm) of a number.

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
      i = 12
      py5.println(py5.log(i))
      py5.println(log10(i))

      j = -5
      py5.println(py5.log(j))

    # Calculates the base-10 logarithm of a number
    # use this if you don't want to use numpy's log10 function
    def log10(x):
        return (py5.log(x) / py5.log(10))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Calculates the natural logarithm (the base-e logarithm) of a number. This function expects the ``n`` parameter to be a value greater than 0.0. This function is the compliment to :doc:`exp`.

This function makes a call to the numpy ``log()`` function. If the ``n`` parameter is less than or equal to 0.0, you will see a ``RuntimeWarning`` and the returned result will be numpy's Not-a-Number value, ``np.nan``.

Syntax
======

.. code:: python

    log(value: float) -> float

Parameters
==========

* **value**: `float` - number greater than 0.0


Updated on July 06, 2021 22:46:12pm UTC

