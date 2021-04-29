.. title: render_frame_sequence()
.. slug: render_frame_sequence
.. date: 2021-04-29 20:23:09 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 render_frame_sequence() documentation
.. type: text

Helper function to render a sequence of frames using the passed ``draw`` function argument.

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

    def draw_counter(s: py5.Sketch):
        s.background(255)
        s.fill(255, 0, 0)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)
        s.text(f'frame number {s.frame_count}', s.width/2, s.height/2)

    frames = py5.render_frame_sequence(draw_counter, 400, 200, limit=10)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup_counter(s: py5.Sketch, color=(0,)):
        s.fill(*color)
        s.text_size(20)
        s.text_align(s.CENTER, s.CENTER)


    def draw_counter(s: py5.Sketch, message_prefix):
        s.background(255)
        s.text(f'{message_prefix} {s.frame_count}', s.width/2, s.height/2)


    frames = py5.render_frame_sequence(draw_counter, 400, 200, py5.P2D,
                                       limit=10,
                                       setup=setup_counter,
                                       setup_kwargs=dict(color=(255, 0, 0)),
                                       draw_args=('sequential numbers:',))

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def random_squares(g: py5.Py5Graphics):
        for _ in range(10):
            g.rect(np.random.randint(g.width), np.random.randint(g.height), 10, 10)

    frames = py5.render_frame_sequence(random_squares, 100, 100, limit=10, use_py5graphics=True)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Helper function to render a sequence of frames using the passed ``draw`` function argument. The output is returned as a list of ``PIL.Image`` objects. Use the ``limit`` keyword argument to specify the number of frames to return.

The passed ``draw`` function's first parameter must be either a ``py5.Sketch`` object or a ``py5.Py5Graphics`` object, depending on the parameter ``use_py5graphics``. That object must be used for all py5 commands. The function can have additional positional and keyword arguments. To use them, pass the desired values to ``render_frame_sequence``'s ``draw_args`` and ``draw_kwargs`` arguments.

Currently, only the default and OpenGL renderers are supported.

The rendered frames can have transparent pixels if and only if the ``use_py5graphics`` parameter is ``True`` because only a ``py5.Py5Graphics`` object can create an image with transparency. If you need to clear the canvas between one frame and the next, use :doc:`py5graphics_clear`. There is no need to call :doc:`py5graphics_begin_draw` or :doc:`py5graphics_end_draw` in the passed ``draw`` function as ``render_frame_sequence()`` does that for you.

Optionally the caller can pass a ``setup`` function, along with corresponding ``setup_args`` and ``setup_kwargs`` arguments. This will be called once, just like it would for any other py5 Sketch. The type of the first parameter must also depend on the ``use_py5graphics`` parameter.

This function facilitates the creation and execution of a py5 Sketch, and as a result makes it easy to run a Sketch inside of another Sketch. This is discouraged, and may fail catastrophically.

This function is available in decorator form as :doc:`render_sequence`.

Syntax
======

.. code:: python

    render_frame_sequence(draw: Callable, width: int, height: int, renderer: str = Sketch.HIDDEN, *, limit: int = 1, setup: Callable = None, setup_args: Tuple = None, setup_kwargs: Dict = None, draw_args: Tuple = None, draw_kwargs: Dict = None, use_py5graphics: bool = False) -> List[PIL_Image]

Parameters
==========

* **draw**: `Callable` - function that executes py5 draw commands
* **draw_args**: `Tuple = None` - additional positional arguments to pass to draw function
* **draw_kwargs**: `Dict = None` - additional keyword arguments to pass to draw function
* **height**: `int` - height of the display window in units of pixels
* **limit**: `int = 1` - number of frames in the output sequence
* **renderer**: `str = Sketch.HIDDEN` - rendering engine to use
* **setup**: `Callable = None` - function that executes py5 setup commands
* **setup_args**: `Tuple = None` - additional positional arguments to pass to setup function
* **setup_kwargs**: `Dict = None` - additional keyword arguments to pass to setup function
* **use_py5graphics**: `bool = False` - pass a py5graphics object instead of a sketch object
* **width**: `int` - width of the display window in units of pixels


Updated on April 29, 2021 20:23:09pm UTC

