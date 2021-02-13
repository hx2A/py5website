.. title: frame_rate()
.. slug: frame_rate
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 frame_rate() documentation
.. type: text

Specifies the number of frames to be displayed every second.

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

    pos = 0


    def setup():
        py5.frame_rate(4)


    def draw():
        py5.background(204)
        global pos
        pos += 1
        py5.line(pos, 20, pos, 80)
        if pos > py5.width:
            pos = 0

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Specifies the number of frames to be displayed every second. For example, the function call ``frame_rate(30)`` will attempt to refresh 30 times a second. If the processor is not fast enough to maintain the specified rate, the frame rate will not be achieved. Setting the frame rate within ``setup()`` is recommended. The default rate is 60 frames per second.

Underlying Java method: `frameRate <https://processing.org/reference/frameRate_.html>`_

Syntax
======

.. code:: python

    frame_rate(fps: float, /) -> None

Parameters
==========

* **fps**: `float` - number of desired frames per second


Updated on February 13, 2021 18:02:35pm UTC

