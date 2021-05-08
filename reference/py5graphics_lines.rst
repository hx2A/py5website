.. title: Py5Graphics.lines()
.. slug: py5graphics_lines
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.lines() documentation
.. type: text

Draw a collection of lines to the Py5Graphics drawing surface.

Description
===========

Draw a collection of lines to the Py5Graphics drawing surface. The purpose of this method is to provide an alternative to repeatedly calling :doc:`py5graphics_line` in a loop. For a large number of lines, the performance of ``lines()`` will be much faster.

The ``coordinates`` parameter should be a numpy array with one row for each line. The first few columns are for the first point of each line and the next few columns are for the second point of each line. There will be four or six columns for 2D or 3D points, respectively.

This method is the same as :doc:`lines` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`lines`.

Underlying Java method: PGraphics.lines

Syntax
======

.. code:: python

    lines(coordinates: NDArray[(Any, Any), Float], /) -> None

Parameters
==========

* **coordinates**: `NDArray[(Any, Any), Float]` - array of line coordinates


Updated on May 06, 2021 16:39:27pm UTC

