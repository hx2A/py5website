.. title: py5_tools.screenshot()
.. slug: screenshot
.. date: 2021-06-14 01:04:37 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 py5_tools.screenshot() documentation
.. type: text

Take a screenshot of a running Sketch.

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

    import time
    import py5_tools

    py5.run_sketch()
    # take a screenshot of the running sketch after a two second delay
    time.sleep(2)
    img = py5_tools.screenshot()
    img.save('image.png')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Take a screenshot of a running Sketch.

The returned image is a ``PIL.Image`` object. It can be assigned to a variable or embedded in the notebook.

By default the Sketch will be the currently running Sketch, as returned by :doc:`get_current_sketch`. Use the ``sketch`` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw`` parameter to make this function run after ``post_draw()`` instead of ``draw()``. This is important when using Processing libraries that support ``post_draw()`` such as Camera3D or ColorBlindness.

Syntax
======

.. code:: python

    screenshot(*, sketch: Sketch = None, hook_post_draw: bool = False) -> PIL.Image

Parameters
==========

* **hook_post_draw**: `bool = False` - attach hook to Sketch's post_draw method instead of draw
* **sketch**: `Sketch = None` - running Sketch


Updated on June 14, 2021 01:04:37am UTC

