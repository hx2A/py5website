.. title: @render()
.. slug: render
.. date: 2021-03-05 15:12:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 @render() documentation
.. type: text

Decorator function to render a single frame using the decorated ``draw`` function.

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

    @py5.render(400, 200)
    def draw_message(s: py5.Sketch):
        s.background(255)
        s.fill(255, 0, 0)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text('hello world', s.width/2, s.height/2)

    frame = draw_message()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    @py5.render(400, 200, py5.P2D)
    def draw_message(s: py5.Sketch, message='hello world', color=(255, 0, 0)):
        s.background(255)
        s.fill(*color)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text(message, s.width/2, s.height/2)

    frame = draw_message('I LIKE ORANGE THINGS', color=(255, 128, 0))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Decorator function to render a single frame using the decorated ``draw`` function. The output is returned as a ``PIL.Image`` object.

The decorated draw function's first parameter must be a ``py5.Sketch`` object, and that object must be used for all of the function's py5 commands. The function can have additional positional and keyword arguments. To use them, pass the desired values when you call the decorated function as you would to any other Python function.

Currently, only the default and OpenGL renderers are supported.

This function facilitates the creation and execution of a py5 Sketch, and as a result makes it easy to run a Sketch inside of another Sketch. This is discouraged, and may fail catastrophically.

This function is available in non-decorator form as :doc:`render_frame`.

Syntax
======

.. code:: python

    render(width: int, height: int, renderer: str = Sketch.HIDDEN) -> Image

Parameters
==========

* **height**: `int` - height of the display window in units of pixels
* **renderer**: `str = Sketch.HIDDEN` - rendering engine to use
* **width**: `int` - width of the display window in units of pixels


Updated on March 05, 2021 15:12:39pm UTC

