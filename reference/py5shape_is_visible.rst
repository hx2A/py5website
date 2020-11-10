.. title: is_visible()
.. slug: py5shape_is_visible
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 is_visible() documentation
.. type: text

Returns a boolean value "true" if the image is set to be visible, "false" if not.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_is_visible_0.png
    :alt: example picture for is_visible()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        size(100, 100)
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = load_shape("bot.svg")


    def draw():
        background(204)
        shape(s, 10, 10, 80, 80)  # draw shape
        s.set_visible(is_mouse_pressed())
        if s.is_visible() == False:  # or use: "if (!s.isVisible)"
            no_fill()
            rect(10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns a boolean value "true" if the image is set to be visible, "false" if not. This value can be modified with the ``set_visible()`` method.

The default visibility of a shape is usually controlled by whatever program created the SVG file. For instance, this parameter is controlled by showing or hiding the shape in the layers palette in Adobe Illustrator.

Underlying Java method: `PShape.isVisible <https://processing.org/reference/PShape_isVisible_.html>`_

Syntax
======

.. code:: python

    is_visible() -> bool

Updated on January 01, 1970 00:00:00am UTC

