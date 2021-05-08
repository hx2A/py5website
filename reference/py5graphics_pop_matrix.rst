.. title: Py5Graphics.pop_matrix()
.. slug: py5graphics_pop_matrix
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.pop_matrix() documentation
.. type: text

Pops the current transformation matrix off the matrix stack.

Description
===========

Pops the current transformation matrix off the matrix stack. Understanding pushing and popping requires understanding the concept of a matrix stack. The :doc:`py5graphics_push_matrix` function saves the current coordinate system to the stack and ``pop_matrix()`` restores the prior coordinate system. :doc:`py5graphics_push_matrix` and ``pop_matrix()`` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

This method is the same as :doc:`pop_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`pop_matrix`.

Underlying Java method: PGraphics.popMatrix

Syntax
======

.. code:: python

    pop_matrix() -> None

Updated on May 04, 2021 20:06:05pm UTC

