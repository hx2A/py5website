.. title: loop()
.. slug: loop
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 loop() documentation
.. type: text

By default, py5 loops through ``draw()`` continuously, executing the code within it.

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

    x = 0


    def setup():
        py5.size(200, 200)
        py5.no_loop()  # draw() will not loop


    def draw():
        global x
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

By default, py5 loops through ``draw()`` continuously, executing the code within it. However, the ``draw()`` loop may be stopped by calling :doc:`no_loop`. In that case, the ``draw()`` loop can be resumed with ``loop()``.

Underlying Java method: `loop <https://processing.org/reference/loop_.html>`_

Syntax
======

.. code:: python

    loop() -> None

Updated on June 28, 2021 15:16:14pm UTC

