.. title: size()
.. slug: size
.. date: 2021-03-05 15:24:25 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 size() documentation
.. type: text

Defines the dimension of the display window width and height in units of pixels.

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

    def settings():
        py5.size(200, 100)


    def setup():
        py5.background(153)
        py5.line(0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(320, 240)


    def draw():
        py5.background(153)
        py5.line(0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(150, 200, py5.P3D)  # specify P3D renderer


    def setup():
        py5.background(153)
    
        # with P3D, we can use z (depth) values...
        py5.line(0, 0, 0, py5.width, py5.height, -100)
        py5.line(py5.width, 0, 0, py5.width, py5.height, -100)
        py5.line(0, py5.height, 0, py5.width, py5.height, -100)
    
        # ...and 3D-specific functions, like box()
        py5.translate(py5.width//2, py5.height//2)
        py5.rotate_x(py5.PI/6)
        py5.rotate_y(py5.PI/6)
        py5.box(35)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Defines the dimension of the display window width and height in units of pixels. This must be called from the ``settings()`` function.

The built-in variables :doc:`width` and :doc:`height` are set by the parameters passed to this function. For example, running ``size(640, 480)`` will assign 640 to the :doc:`width` variable and 480 to the height ``variable``. If ``size()`` is not used, the window will be given a default size of 100 x 100 pixels.

The ``size()`` function can only be used once inside a sketch, and it cannot be used for resizing.

To run a sketch at the full dimensions of a screen, use the :doc:`full_screen` function, rather than the older way of using ``size(display_width, display_height)``.

The maximum width and height is limited by your operating system, and is usually the width and height of your actual screen. On some machines it may simply be the number of pixels on your current screen, meaning that a screen of 800 x 600 could support ``size(1600, 300)``, since that is the same number of pixels. This varies widely, so you'll have to try different rendering modes and sizes until you get what you're looking for. If you need something larger, use ``create_graphics`` to create a non-visible drawing surface.

The minimum width and height is around 100 pixels in each direction. This is the smallest that is supported across Windows, macOS, and Linux. We enforce the minimum size so that sketches will run identically on different machines.

The ``renderer`` parameter selects which rendering engine to use. For example, if you will be drawing 3D shapes, use ``P3D``. In addition to the default renderer, other renderers are:

* ``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-compatible graphics hardware.
* ``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-compatible graphics hardware.
* ``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for some applications, but has some compatibility quirks.
* ``PDF``: The ``PDF`` renderer draws 2D graphics directly to an Acrobat PDF file. This produces excellent results when you need vector shapes for high-resolution output or printing.
* ``SVG``: The ``SVG`` renderer draws 2D graphics directly to an SVG file. This is great for importing into other vector programs or using for digital fabrication.

Underlying Java method: `size <https://processing.org/reference/size_.html>`_

Syntax
======

.. code:: python

    size(width: int, height: int, /) -> None
    size(width: int, height: int, renderer: str, /) -> None
    size(width: int, height: int, renderer: str, path: str, /) -> None

Parameters
==========

* **height**: `int` - height of the display window in units of pixels
* **path**: `str` - filename to save rendering engine output to
* **renderer**: `str` - rendering engine to use
* **width**: `int` - width of the display window in units of pixels


Updated on March 05, 2021 15:24:25pm UTC

