.. title: loop()
.. slug: loop
.. date: 2021-02-13 18:02:35 UTC+00:00
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
        py5.size(200, 200)
        py5.no_loop()  # draw() will not loop


    x = 0


    def draw():
        py5.background(204)
        x = x + .1
        if x > py5.width:
            x = 0

        py5.line(x, 0, x, py5.height)


    def mouse_pressed():
        py5.loop()  # holding down the mouse activates looping


    def mouse_released():
        py5.no_loop()  # releasing the mouse stops looping draw()

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

Updated on February 13, 2021 18:02:35pm UTC

