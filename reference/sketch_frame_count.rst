.. title: frame_count
.. slug: sketch_frame_count
.. date: 2020-11-03 22:19:57 UTC+00:00
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


Updated on November 03, 2020 22:19:57pm UTC

