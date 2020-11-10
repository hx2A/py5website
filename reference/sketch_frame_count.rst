.. title: frame_count
.. slug: frame_count
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 frame_count documentation
.. type: text

The system variable ``frame_count`` contains the number of frames that have been displayed since the program started.

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
        frame_rate(30)


    def draw():
        line(0, 0, width, height)
        print(frame_count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The system variable ``frame_count`` contains the number of frames that have been displayed since the program started. Inside ``setup()`` the value is 0, after the first iteration of draw it is 1, etc.

Underlying Java field: `frameCount <https://processing.org/reference/frameCount.html>`_


Updated on January 01, 1970 00:00:00am UTC

