.. title: push_style()
.. slug: push_style
.. date: 2021-03-05 15:24:25 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 push_style() documentation
.. type: text

The ``push_style()`` function saves the current style settings and :doc:`pop_style` restores the prior settings.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_style_0.png
    :alt: example picture for push_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        py5.push_style()  # start a new style
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(50, 50, 33, 33)  # middle circle
        py5.pop_style()  # restore original style
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_push_style_1.png
    :alt: example picture for push_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.ellipse(0, 50, 33, 33)  # left circle
    
        py5.push_style()  # start a new style
        py5.stroke_weight(10)
        py5.fill(204, 153, 0)
        py5.ellipse(33, 50, 33, 33)  # left-middle circle
    
        py5.push_style()  # start another new style
        py5.stroke(0, 102, 153)
        py5.ellipse(66, 50, 33, 33)  # right-middle circle
        py5.pop_style()  # restore previous style
    
        py5.pop_style()  # restore original style
    
        py5.ellipse(100, 50, 33, 33)  # right circle

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``push_style()`` function saves the current style settings and :doc:`pop_style` restores the prior settings. Note that these functions are always used together. They allow you to change the style settings and later return to what you had. When a new style is started with ``push_style()``, it builds on the current style information. The ``push_style()`` and :doc:`pop_style` functions can be embedded to provide more control. (See the second example for a demonstration.)

The style information controlled by the following functions are included in the style: :doc:`fill`, :doc:`stroke`, :doc:`tint`, :doc:`stroke_weight`, :doc:`stroke_cap`, :doc:`stroke_join`, :doc:`image_mode`, :doc:`rect_mode`, :doc:`ellipse_mode`, :doc:`shape_mode`, :doc:`color_mode`, :doc:`text_align`, :doc:`text_font`, :doc:`text_mode`, :doc:`text_size`, :doc:`text_leading`, :doc:`emissive`, :doc:`specular`, :doc:`shininess`, and :doc:`ambient`.

Underlying Java method: `pushStyle <https://processing.org/reference/pushStyle_.html>`_

Syntax
======

.. code:: python

    push_style() -> None

Updated on March 05, 2021 15:24:25pm UTC

