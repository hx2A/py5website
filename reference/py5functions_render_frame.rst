.. title: render_frame()
.. slug: render_frame
.. date: 2021-02-02 21:26:46 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 render_frame() documentation
.. type: text

Helper function to render a single frame using the passed ``draw`` function argument.

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

    def draw_message(s: py5.Sketch):
        s.background(255)
        s.fill(255, 0, 0)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text('hello world', s.width / 2, s.height / 2)

    frame = py5.render_frame(draw_message, 400, 200)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def draw_message(s: py5.Sketch, message='hello world', color=(255, 0, 0)):
        s.background(255)
        s.fill(*color)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text(message, s.width / 2, s.height / 2)

    frame = py5.render_frame(draw_message, 400, 200, py5.P2D,
                             draw_args=('I LIKE ORANGE THINGS',),
                             draw_kwargs=dict(color=(255, 128, 0)))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Helper function to render a single frame using the passed ``draw`` function argument. The output is returned as a ``PIL.Image`` object.

The passed function's first parameter must be a ``py5.Sketch`` object, and that object must be used for all of the function's py5 commands. The function can have additional positional and keyword arguments. To use them, pass the desired values as ``render_frame``'s ``draw_args`` and ``draw_kwargs`` arguments.

Currently, only the default and OpenGL renderers are supported.

This function facilitates the creation and execution of a py5 Sketch, and as a result makes it easy to run a Sketch inside of another Sketch. This is discouraged, and may fail catastrophically.

This function is available in decorator form as :doc:`render`.

Syntax
======

.. code:: python

    render_frame(draw: Callable, width: int, height: int, renderer: str = Sketch.HIDDEN, *, draw_args: Tuple = None, draw_kwargs: Dict = None) -> Image

Parameters
==========

* **draw**: `Callable` - function that executes py5 draw commands
* **draw_args**: `Tuple = None` - additional positional arguments to pass to draw function
* **draw_kwargs**: `Dict = None` - additional keyword arguments to pass to draw function
* **height**: `int` - height of the display window in units of pixels
* **renderer**: `str = Sketch.HIDDEN` - rendering engine to use
* **width**: `int` - width of the display window in units of pixels


Updated on February 02, 2021 21:26:46pm UTC

