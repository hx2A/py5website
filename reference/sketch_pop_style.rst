.. title: pop_style()
.. slug: sketch_pop_style
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pop_style() documentation
.. type: text

The ``push_style()`` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_style_0.png
    :alt: example picture for pop_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    ellipse(0, 50, 33, 33)  # left circle

    push_style()  # start a new style
    stroke_weight(10)
    fill(204, 153, 0)
    ellipse(50, 50, 33, 33)  # middle circle
    pop_style()  # restore original style

    ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_pop_style_1.png
    :alt: example picture for pop_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    ellipse(0, 50, 33, 33)  # left circle

    push_style()  # start a new style
    stroke_weight(10)
    fill(204, 153, 0)
    ellipse(33, 50, 33, 33)  # left-middle circle

    push_style()  # start another new style
    stroke(0, 102, 153)
    ellipse(66, 50, 33, 33)  # right-middle circle
    pop_style()  # restore the previous style

    pop_style()  # restore original style

    ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``push_style()`` function saves the current style settings and ``pop_style()`` restores the prior settings; these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with ``push_style()``, it builds on the current style information. The ``push_style()`` and ``pop_style()`` functions can be embedded to provide more control (see the second example above for a demonstration.)

Syntax
======

.. code:: python

    pop_style() -> None

Updated on November 03, 2020 22:19:57pm UTC

