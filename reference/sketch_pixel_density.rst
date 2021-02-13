.. title: pixel_density()
.. slug: pixel_density
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pixel_density() documentation
.. type: text

This function is new with Processing 3.0.

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

    def settings():
        py5.pixel_density(2)


    def setup():
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

    def settings():
        py5.pixel_density(py5.display_density())


    def setup():
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

This function is new with Processing 3.0. It makes it possible for Processing to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays. This function can only be run once within a program and it must be called in ``settings()``.  The ``pixel_density()`` should only be used with hardcoded numbers (in almost all cases this number will be 2) or in combination with ``display_density()`` as in the second example above.

When the pixel density is set to more than 1, it changes all of the pixel operations including the way ``get()``, ``set()``, ``blend()``, ``copy()``, and ``update_pixels()`` all work. See the reference for ``pixel_width`` and ``pixel_height`` for more information. 

To use variables as the arguments to ``pixel_density()`` function, place the ``pixel_density()`` function within the ``settings()`` function. There is more information about this on the ``settings()`` reference page.

Underlying Java method: `pixelDensity <https://processing.org/reference/pixelDensity_.html>`_

Syntax
======

.. code:: python

    pixel_density(density: int, /) -> None

Parameters
==========

* **density**: `int` - 1 or 2


Updated on February 13, 2021 18:02:35pm UTC

