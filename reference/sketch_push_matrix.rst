.. title: push_matrix()
.. slug: sketch_push_matrix
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 push_matrix() documentation
.. type: text

Pushes the current transformation matrix onto the matrix stack.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_matrix_0.png
    :alt: example picture for push_matrix()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    fill(255)
    rect(0, 0, 50, 50)  # white rectangle

    push_matrix()
    translate(30, 20)
    fill(0)
    rect(0, 0, 50, 50)  # black rectangle
    pop_matrix()

    fill(100)
    rect(15, 10, 50, 50)  # gray rectangle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Pushes the current transformation matrix onto the matrix stack. Understanding ``push_matrix()`` and ``pop_matrix()`` requires understanding the concept of a matrix stack. The ``push_matrix()`` function saves the current coordinate system to the stack and ``pop_matrix()`` restores the prior coordinate system. ``push_matrix()`` and ``pop_matrix()`` are used in conjuction with the other transformation functions and may be embedded to control the scope of the transformations.

Syntax
======

.. code:: python

    push_matrix() -> None

Updated on November 03, 2020 22:19:57pm UTC

