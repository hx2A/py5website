.. title: %py5animatedgif
.. slug: py5animatedgif
.. date: 2021-03-03 21:29:41 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 %py5animatedgif documentation
.. type: text

Create an animated GIF using the currently running sketch.

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

    py5.run_sketch()
    # create a 10 frame animated GIF saved to '/tmp/animated.gif'
    %py5animatedgif /tmp/animated.gif 10 1 0.5 -w 3

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Create an animated GIF using the currently running sketch.

Use the ``-w`` argument to wait before starting.

Usage
=====

.. code::

    %py5animatedgif [-w WAIT] [-l LOOP] [--optimize] filename count period duration

Arguments
=========

.. code::

    positional arguments:
      filename              filename of GIF to create
      count                 number of Sketch snapshots to create
      period                time in seconds between Sketch snapshots
      duration              time in seconds between frames in the GIF

    optional arguments:
      -w WAIT, --wait WAIT  wait time in seconds before starting sketch frame capture
      -l LOOP, --loop LOOP  number of times for the GIF to loop (default of 0 loops indefinitely)
      --optimize            optimize GIF palette

Updated on March 03, 2021 21:29:41pm UTC

