.. title: py5_tools.capture_frames()
.. slug: capture_frames
.. date: 2021-06-14 01:04:37 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 py5_tools.capture_frames() documentation
.. type: text

Capture frames from a running Sketch.

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

    import py5_tools

    py5.run_sketch()
    # capture 10 frames from the currently running sketch
    frames = py5_tools.capture_frames(10, period=1)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Capture frames from a running Sketch.

By default the Sketch will be the currently running Sketch, as returned by :doc:`get_current_sketch`. Use the ``sketch`` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw`` parameter to make this function run after ``post_draw()`` instead of ``draw()``. This is important when using Processing libraries that support ``post_draw()`` such as Camera3D or ColorBlindness.

Syntax
======

.. code:: python

    capture_frames(count: float, *, period: float = 0.0, sketch: Sketch = None, hook_post_draw: bool = False) -> List[PIL.Image]

Parameters
==========

* **count**: `float` - number of Sketch snapshots to capture
* **hook_post_draw**: `bool = False` - attach hook to Sketch's post_draw method instead of draw
* **period**: `float = 0.0` - time in seconds between Sketch snapshots (default 0 means no delay)
* **sketch**: `Sketch = None` - running Sketch


Updated on June 14, 2021 01:04:37am UTC

