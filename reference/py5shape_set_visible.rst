.. title: set_visible()
.. slug: py5shape_set_visible
.. date: 2021-03-04 18:12:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_visible() documentation
.. type: text

Sets the shape to be visible or invisible.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = py5.load_shape("bot.svg")


    def draw():
        py5.background(204)
        py5.shape(s, 10, 10, 80, 80)  # draw shape
        s.set_visible(py5.is_mouse_pressed)
        if s.is_visible() == False:  # or use: "if (!s.isVisible)"
            py5.no_fill()
            py5.rect(10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the shape to be visible or invisible. This is determined by the value of the ``visible`` parameter.

The default visibility of a shape is usually controlled by whatever program created the SVG file. For instance, this parameter is controlled by showing or hiding the shape in the layers palette in Adobe Illustrator.

Underlying Java method: `PShape.setVisible <https://processing.org/reference/PShape_setVisible_.html>`_

Syntax
======

.. code:: python

    set_visible(visible: bool, /) -> None

Parameters
==========

* **visible**: `bool` - ``False`` makes the shape invisible and ``True`` makes it visible


Updated on March 04, 2021 18:12:39pm UTC

