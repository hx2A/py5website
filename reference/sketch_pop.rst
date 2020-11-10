.. title: pop()
.. slug: pop
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pop() documentation
.. type: text

The ``pop()`` function restores the previous drawing style settings and transformations after ``push()`` has changed them.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_0.png
    :alt: example picture for pop()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    fill(255)
    rect(0, 0, 50, 50)  # white rectangle

    push()
    translate(30, 20)
    fill(0)
    rect(0, 0, 50, 50)  # black rectangle
    pop()  # restore original settings

    fill(100)
    rect(15, 10, 50, 50)  # gray rectangle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_1.png
    :alt: example picture for pop()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    ellipse(0, 50, 33, 33)  # left circle

    push()
    stroke_weight(10)
    fill(204, 153, 0)
    ellipse(50, 50, 33, 33)  # middle circle
    pop()  # restore original settings

    ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``pop()`` function restores the previous drawing style settings and transformations after ``push()`` has changed them. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with ``push()``, it builds on the current style and transform information.

``push()`` stores information related to the current transformation state and style settings controlled by the following functions: ``rotate()``, ``translate()``, ``scale()``, ``fill()``, ``stroke()``, ``tint()``, ``stroke_weight()``, ``stroke_cap()``, ``stroke_join()``, ``image_mode()``, ``rect_mode()``, ``ellipse_mode()``, ``color_mode()``, ``text_align()``, ``text_font()``, ``text_mode()``, ``text_size()``, ``text_leading()``.

The ``push()`` and ``pop()`` functions were added with Processing 3.5. They can be used in place of ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and ``pop_styles()``. The difference is that ``push()`` and ``pop()`` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

Underlying Java method: `pop <https://processing.org/reference/pop_.html>`_

Syntax
======

.. code:: python

    pop() -> None

Updated on November 10, 2020 15:41:45pm UTC

