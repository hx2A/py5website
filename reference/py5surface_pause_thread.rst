.. title: Py5Surface.pause_thread()
.. slug: py5surface_pause_thread
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Surface.pause_thread() documentation
.. type: text

Pause a running Sketch.

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

    def draw():
        py5.rect(py5.random(py5.width), py5.random(py5.height), 10, 10)
        print(py5.frame_count)

    py5.run_sketch(block=False)
    surface = py5.get_surface()

    # pause the sketch.
    surface.pause_thread()
    # the sketch is no longer running and there is no output

    # after waiting a bit, resume the sketch
    surface.resume_thread()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Pause a running Sketch. The Sketch window will be static and unresponsive. You can resume the Sketch with :doc:`py5surface_resume_thread`.

The :doc:`frame_count` will not increment while the Sketch is paused.

Pausing a Sketch is not the same as stopping a Sketch, so this method will not change the results of :doc:`py5surface_is_stopped`.

Underlying Java method: PSurface.pauseThread

Syntax
======

.. code:: python

    pause_thread() -> None

Updated on May 01, 2021 20:51:42pm UTC

