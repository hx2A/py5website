.. title: pixel_density()
.. slug: pixel_density
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pixel_density() documentation
.. type: text

This function makes it possible for py5 to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays.

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
        py5.pixel_density(2)
        py5.no_stroke()


    def draw():
        py5.background(0)
        py5.ellipse(30, 48, 36, 36)
        py5.ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.pixel_density(py5.display_density())
        # pulling the display's density dynamically
        py5.no_stroke()


    def draw():
        py5.background(0)
        py5.ellipse(30, 48, 36, 36)
        py5.ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

This function makes it possible for py5 to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays. This function can only be run once within a program. It is intended to be called from the ``settings()`` function.

When programming in module mode and imported mode, py5 will allow calls to ``pixel_density()`` from the ``setup()`` function if it is called at the beginning of ``setup()``. This allows the user to omit the ``settings()`` function, much like what can be done while programming in the Processing IDE. Py5 does this by inspecting the ``setup()`` function and attempting to split it into synthetic ``settings()`` and ``setup()`` functions if both were not created by the user and the real ``setup()`` function contains a call to ``pixel_density()``, or calls to :doc:`size`, :doc:`full_screen`, :doc:`smooth`, or :doc:`no_smooth`. Calls to those functions must be at the very beginning of ``setup()``, before any other Python code (but comments are ok). This feature is not available when programming in class mode.

The ``pixel_density()`` should only be used with hardcoded numbers (in almost all cases this number will be 2) or in combination with :doc:`display_density` as in the second example.

When the pixel density is set to more than 1, it changes all of the pixel operations including the way :doc:`get`, :doc:`blend`, :doc:`copy`, :doc:`update_pixels`, and :doc:`update_np_pixels` all work. See the reference for :doc:`pixel_width` and :doc:`pixel_height` for more information.

Underlying Java method: `pixelDensity <https://processing.org/reference/pixelDensity_.html>`_

Syntax
======

.. code:: python

    pixel_density(density: int, /) -> None

Parameters
==========

* **density**: `int` - 1 or 2


Updated on June 28, 2021 15:16:14pm UTC

