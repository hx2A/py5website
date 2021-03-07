.. title: %py5captureframes
.. slug: py5captureframes
.. date: 2021-03-06 19:17:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 %py5captureframes documentation
.. type: text

Capture frames from the currently running Sketch.

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
    # capture 10 frames from the currently running sketch
    frames = %py5captureframes 10 -w 3 -p 1

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Capture frames from the currently running Sketch.

Use the ``-w`` argument to wait before starting.

Usage
=====

.. code::

    %py5captureframes [-w WAIT] [-p PERIOD] count

Arguments
=========

.. code::

    positional arguments:
      count                 number of Sketch snapshots to capture

    optional arguments:
      -w WAIT, --wait WAIT  wait time in seconds before starting Sketch frame capture
      -p PERIOD, --period PERIOD
                            time in seconds between Sketch snapshots (default 0 means no delay)

Updated on March 06, 2021 19:17:57pm UTC

