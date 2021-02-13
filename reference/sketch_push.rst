.. title: push()
.. slug: push
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 push() documentation
.. type: text

The ``push()`` function saves the current drawing style settings and transformations, while ``pop()`` restores these settings.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_0.png
    :alt: example picture for push()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.fill(255)
        py5.rect(0, 0, 50, 50)  # white rectangle
    
        py5.push()
        py5.translate(30, 20)
        py5.fill(0)
        py5.rect(0, 0, 50, 50)  # black rectangle
        py5.pop()  # restore original settings
    
        py5.fill(100)
        py5.rect(15, 10, 50, 50)  # gray rectangle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_1.png
    :alt: example picture for push()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        py5.push()
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(50, 50, 33, 33)  # middle circle
        py5.pop()  # restore original settings
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``push()`` function saves the current drawing style settings and transformations, while ``pop()`` restores these settings. Note that these functions are always used together. They allow you to change the style and transformation settings and later return to what you had. When a new state is started with ``push()``, it builds on the current style and transform information.

``push()`` stores information related to the current transformation state and style settings controlled by the following functions: ``rotate()``, ``translate()``, ``scale()``, ``fill()``, ``stroke()``, ``tint()``, ``stroke_weight()``, ``stroke_cap()``, ``stroke_join()``, ``image_mode()``, ``rect_mode()``, ``ellipse_mode()``, ``color_mode()``, ``text_align()``, ``text_font()``, ``text_mode()``, ``text_size()``, ``text_leading()``.

The ``push()`` and ``pop()`` functions were added with Processing 3.5. They can be used in place of ``push_matrix()``, ``pop_matrix()``, ``push_styles()``, and ``pop_styles()``. The difference is that ``push()`` and ``pop()`` control both the transformations (rotate, scale, translate) and the drawing styles at the same time.

Underlying Java method: `push <https://processing.org/reference/push_.html>`_

Syntax
======

.. code:: python

    push() -> None

Updated on February 13, 2021 18:02:35pm UTC

