.. title: frame_rate()
.. slug: sketch_frame_rate
.. date: 2020-11-04 20:45:44 UTC+00:00
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

    def setup():
        frame_rate(4)


    pos = 0


    def draw():
        background(204)
        pos++
        line(pos, 20, pos, 80)
        if pos > width:
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

    frame_rate(fps: float) -> None

Parameters
==========

* **fps**: `float` - number of desired frames per second


Updated on November 04, 2020 20:45:44pm UTC

