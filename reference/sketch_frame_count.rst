.. title: frame_count
.. slug: frame_count
.. date: 2021-02-13 18:02:35 UTC+00:00
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
        py5.frame_rate(30)


    def draw():
        py5.line(0, 0, py5.width, py5.height)
        print(py5.frame_count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The system variable ``frame_count`` contains the number of frames that have been displayed since the program started. Inside ``setup()`` the value is 0, after the first iteration of draw it is 1, etc.

Underlying Java field: `frameCount <https://processing.org/reference/frameCount.html>`_


Updated on February 13, 2021 18:02:35pm UTC

