.. title: no_loop()
.. slug: no_loop
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_loop() documentation
.. type: text

Stops Processing from continuously executing the code within ``draw()``.

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
        py5.size(200, 200)


    def setup():
        py5.no_loop()


    def draw():
        py5.line(10, 10, 190, 190)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    x = 0.0


    def settings():
        py5.size(200, 200)


    def draw():
        py5.background(204)
        global x
        x = x + 0.1
        if x > py5.width:
            x = 0
        py5.line(x, 0, x, py5.height)


    def mouse_pressed():
        py5.no_loop()


    def mouse_released():
        py5.loop()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    some_mode = False


    def setup():
        py5.no_loop()


    def draw():
        if some_mode:
            # do something
            pass


    def mouse_pressed():
        some_mode = True
        py5.redraw()  # or call loop()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Stops Processing from continuously executing the code within ``draw()``. If ``loop()`` is called, the code in ``draw()`` begins to run continuously again. If using ``no_loop()`` in ``setup()``, it should be the last line inside the block.

When ``no_loop()`` is used, it's not possible to manipulate or access the screen inside event handling functions such as ``mouse_pressed()`` or ``key_pressed()``. Instead, use those functions to call ``redraw()`` or ``loop()``, which will run ``draw()``, which can update the screen properly. This means that when ``no_loop()`` has been called, no drawing can happen, and functions like ``save_frame()`` or ``load_pixels()`` may not be used.

Note that if the sketch is resized, ``redraw()`` will be called to update the sketch, even after ``no_loop()`` has been specified. Otherwise, the sketch would enter an odd state until ``loop()`` was called.

Underlying Java method: `noLoop <https://processing.org/reference/noLoop_.html>`_

Syntax
======

.. code:: python

    no_loop() -> None

Updated on February 13, 2021 18:02:35pm UTC

