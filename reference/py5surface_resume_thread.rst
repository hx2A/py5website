.. title: Py5Surface.resume_thread()
.. slug: py5surface_resume_thread
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Surface.resume_thread() documentation
.. type: text

Resume a paused Sketch.

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
        py5.println(py5.frame_count)

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

Resume a paused Sketch. The Sketch window will resume operating as it did before :doc:`py5surface_pause_thread` was called.

The :doc:`frame_count` will continue incrementing after the Sketch is resumed.

Underlying Java method: PSurface.resumeThread

Syntax
======

.. code:: python

    resume_thread() -> None

Updated on July 06, 2021 22:46:12pm UTC

