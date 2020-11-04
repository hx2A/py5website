.. title: loop()
.. slug: sketch_loop
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 loop() documentation
.. type: text

By default, Processing loops through ``draw()`` continuously, executing the code within it.

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
        no_loop()  # draw() will not loop


    x = 0


    def draw():
        background(204)
        x = x + .1
        if x > width:
            x = 0

        line(x, 0, x, height)


    def mouse_pressed():
        loop()  # holding down the mouse activates looping


    def mouse_released():
        no_loop()  # releasing the mouse stops looping draw()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

By default, Processing loops through ``draw()`` continuously, executing the code within it. However, the ``draw()`` loop may be stopped by calling ``no_loop()``. In that case, the ``draw()`` loop can be resumed with ``loop()``.

Underlying Java method: `loop <https://processing.org/reference/loop_.html>`_

Syntax
======

.. code:: python

    loop() -> None

Updated on November 04, 2020 20:45:44pm UTC

