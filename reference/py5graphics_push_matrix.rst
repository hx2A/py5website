.. title: Py5Graphics.push_matrix()
.. slug: py5graphics_push_matrix
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.push_matrix() documentation
.. type: text

Pushes the current transformation matrix onto the matrix stack.

Description
===========

Pushes the current transformation matrix onto the matrix stack. Understanding ``push_matrix()`` and :doc:`py5graphics_pop_matrix` requires understanding the concept of a matrix stack. The ``push_matrix()`` function saves the current coordinate system to the stack and :doc:`py5graphics_pop_matrix` restores the prior coordinate system. ``push_matrix()`` and :doc:`py5graphics_pop_matrix` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

This method is the same as :doc:`push_matrix` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`push_matrix`.

Underlying Java method: PGraphics.pushMatrix

Syntax
======

.. code:: python

    push_matrix() -> None

Updated on May 04, 2021 20:06:05pm UTC

