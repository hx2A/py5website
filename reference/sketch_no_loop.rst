.. title: no_loop()
.. slug: sketch_no_loop
.. date: 2020-11-04 20:45:44 UTC+00:00
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

    def setup():
        size(200, 200)
        no_loop()


    def draw():
        line(10, 10, 190, 190)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(200, 200)


    x = 0.0


    def draw():
        background(204)
        x = x + 0.1
        if x > width:
            x = 0

        line(x, 0, x, height)


    def mouse_pressed():
        no_loop()


    def mouse_released():
        loop()

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
        no_loop()


    def draw():
        if some_mode:
            # do something


    def mouse_pressed():
        some_mode = True
        redraw()  # or loop()

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

Updated on November 04, 2020 20:45:44pm UTC

