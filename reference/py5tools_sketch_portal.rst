.. title: py5_tools.sketch_portal()
.. slug: sketch_portal
.. date: 2021-08-03 18:51:54 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 py5_tools.sketch_portal() documentation
.. type: text

Creates a portal widget to continuously stream frames from a running Sketch into a Jupyter notebook.

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
    # stream frames from the currently running sketch for 5 seconds
    portal = py5_tools.sketch_portal(time_limit=5)

    portal

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Creates a portal widget to continuously stream frames from a running Sketch into a Jupyter notebook. Each frame will appear embedded in the notebook, with each new frame replacing the previous frame.

By default the Sketch will be the currently running Sketch, as returned by :doc:`get_current_sketch`. Use the ``sketch`` parameter to specify a different running Sketch, such as a Sketch created using Class mode.

The Sketch Portal cannot (currently) handle keyboard or mouse events. As an alternative, consider using Jupyter Widgets for user input.

This magic is intended to be used when a real display is not available, such as when using py5 through an online Jupyter notebook system such as binder. You are free to execute code elsewhere in the notebook while the Sketch is running and the portal is open. This function can only be used in a Jupyter Notebook. It uses ZMQ to stream JPEG images from the kernel to the client front-end.

If you are using Jupyter Lab, try right clicking in the output area of the cell and selecting "Create New View for Output". This will create a new panel just for the Sketch portal. Creating a "New Console for Notebook" and creating a portal there works well also.

This command can be called before :doc:`run_sketch` if the current Sketch is in the :doc:`is_ready` state.

Use the ``time_limit`` parameter to set a time limit (seconds). Use ``throttle_frame_rate`` to throttle the stream's frame rate (frames per second) to a slower pace than the Sketch's actual draw frame rate. By default, ``throttle_frame_rate`` is set to 30, which is half of the Sketch's default draw frame rate of 60 frames per second. Set this parameter to ``None`` to disable throttling. The ``scale`` parameter is a scaling factor that can adjust the portal height and width. The ``quality`` parameter sets the JPEG quality factor (default 75) for the stream, which must be between 1 (worst) and 100 (best). If the portal causes the Sketch's frame rate to drop, try adjusting the portal's throttle frame rate, quality, and scale.

If your Sketch has a ``post_draw()`` method, use the ``hook_post_draw`` parameter to make this function run after ``post_draw()`` instead of ``draw()``. This is important when using Processing libraries that support ``post_draw()`` such as Camera3D or ColorBlindness.

To stop a Sketch portal, wait for the time limit to expire or call :doc:`exit_sketch`. If you delete the cell with the ``Py5SketchPortal`` object, the portal will no longer be visible but the Sketch will still be streaming frames to the notebook client, wasting resources. A Sketch can only have one open portal, so opening a new portal with different options will replace an existing portal.

Syntax
======

.. code:: python

    sketch_portal(*, time_limit: float = 0.0, throttle_frame_rate: float = 30, scale: float = 1.0, quality: int = 75, portal_widget: Py5SketchPortal = None, sketch: Sketch = None, hook_post_draw: bool = False) -> None

Parameters
==========

* **hook_post_draw**: `bool = False` - attach hook to Sketch's post_draw method instead of draw
* **portal_widget**: `Py5SketchPortal = None` - Py5SketchPortal object to send stream to
* **quality**: `int = 75` - JPEG stream quality between 1 (worst) and 100 (best)
* **scale**: `float = 1.0` - scale factor to adjust the height and width of the portal
* **sketch**: `Sketch = None` - running Sketch
* **throttle_frame_rate**: `float = 30` - throttle portal frame rate below Sketch's frame rate
* **time_limit**: `float = 0.0` - time limit in seconds for Sketch portal; set to 0 (default) for no limit


Updated on August 03, 2021 18:51:54pm UTC

