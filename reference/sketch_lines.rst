.. title: lines()
.. slug: lines
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 lines() documentation
.. type: text

Draw a collection of lines to the screen.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lines_0.png
    :alt: example picture for lines()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    import numpy as np

    def setup():
        random_lines = 100 * np.random.rand(50, 4)
        py5.lines(random_lines)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Draw a collection of lines to the screen. The purpose of this method is to provide an alternative to repeatedly calling :doc:`line` in a loop. For a large number of lines, the performance of ``lines()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each line. The first few columns are for the first point of each line and the next few columns are for the second point of each line. There will be four or six columns for 2D or 3D points, respectively.

Underlying Java method: lines

Syntax
======

.. code:: python

    lines(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of line coordinates


Updated on April 06, 2021 18:19:03pm UTC

