.. title: size()
.. slug: size
.. date: 2020-11-24 21:22:32 UTC+00:00
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

    size(200, 100)
    background(153)
    line(0, 0, width, height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(320, 240)


    def draw():
        background(153)
        line(0, 0, width, height)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(150, 200, P3D)  # specify P3D renderer
    background(153)

    # with P3D, we can use z (depth) values...
    line(0, 0, 0, width, height, -100)
    line(width, 0, 0, width, height, -100)
    line(0, height, 0, width, height, -100)

    # ...and 3D-specific functions, like box()
    translate(width//2, height//2)
    rotate_x(PI/6)
    rotate_y(PI/6)
    box(35)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Defines the dimension of the display window width and height in units of pixels. In a program that has the ``setup()`` function, the ``size()`` function must be the first line of code inside ``setup()``, and the ``setup()`` function must appear in the code tab with the same name as your sketch folder.

The built-in variables ``width`` and ``height`` are set by the parameters passed to this function. For example, running ``size(640, 480)`` will assign 640 to the ``width`` variable and 480 to the height ``variable``. If ``size()`` is not used, the window will be given a default size of 100 x 100 pixels.

The ``size()`` function can only be used once inside a sketch, and it cannot be used for resizing.

As of Processing 3, to run a sketch at the full dimensions of a screen, use the ``full_screen()`` function, rather than the older way of using ``size(display_width, display_height)``.

The maximum width and height is limited by your operating system, and is usually the width and height of your actual screen. On some machines it may simply be the number of pixels on your current screen, meaning that a screen of 800 x 600 could support ``size(1600, 300)``, since that is the same number of pixels. This varies widely, so you'll have to try different rendering modes and sizes until you get what you're looking for. If you need something larger, use ``create_graphics`` to create a non-visible drawing surface.

The minimum width and height is around 100 pixels in each direction. This is the smallest that is supported across Windows, macOS, and Linux. We enforce the minimum size so that sketches will run identically on different machines.

The ``renderer`` parameter selects which rendering engine to use. For example, if you will be drawing 3D shapes, use ``P3D``. In addition to the default renderer, other renderers are:

``P2D`` (Processing 2D): 2D graphics renderer that makes use of OpenGL-compatible graphics hardware.

``P3D`` (Processing 3D): 3D graphics renderer that makes use of OpenGL-compatible graphics hardware.

``FX2D`` (JavaFX 2D): A 2D renderer that uses JavaFX, which may be faster for some applications, but has some compatibility quirks.

``PDF``: The PDF renderer draws 2D graphics directly to an Acrobat PDF file. This produces excellent results when you need vector shapes for high-resolution output or printing. You must first use Import Library → PDF to make use of the library. More information can be found in the PDF library reference.

``SVG``: The SVG renderer draws 2D graphics directly to an SVG file. This is great for importing into other vector programs or using for digital fabrication. You must first use Import Library → SVG Export to make use of the library.

As of Processing 3.0, to use variables as the parameters to ``size()`` function, place the ``size()`` function within the ``settings()`` function (instead of ``setup()``). There is more information about this on the ``settings()`` reference page.

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
* **path**: `str` - missing variable description
* **renderer**: `str` - missing variable description
* **width**: `int` - width of the display window in units of pixels


Updated on November 24, 2020 21:22:32pm UTC
