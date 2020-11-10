.. title: pixel_density()
.. slug: pixel_density
.. date: 1970-01-01 00:00:00 UTC+00:00
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

    size(100, 100)
    pixel_density(2)
    no_stroke()
    background(0)
    ellipse(30, 48, 36, 36)
    ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(100, 100)
        pixel_density(2)
        no_stroke()


    def draw():
        background(0)
        ellipse(30, 48, 36, 36)
        ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        size(100, 100)
        # pulling the display's density dynamically
        pixel_density(display_density())
        no_stroke()


    def draw():
        background(0)
        ellipse(30, 48, 36, 36)
        ellipse(70, 48, 36, 36)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

This function is new with Processing 3.0. It makes it possible for Processing to render using all of the pixels on high resolutions screens like Apple Retina displays and Windows High-DPI displays. This function can only be run once within a program and it must be used right after ``size()`` in a program without a ``setup()`` and used within ``setup()`` when a program has one.  The ``pixel_density()`` should only be used with hardcoded numbers (in almost all cases this number will be 2) or in combination with ``display_density()`` as in the third example above.

When the pixel density is set to more than 1, it changes all of the pixel operations including the way ``get()``, ``set()``, ``blend()``, ``copy()``, and ``update_pixels()`` all work. See the reference for ``pixel_width`` and ``pixel_height`` for more information. 

To use variables as the arguments to ``pixel_density()`` function, place the ``pixel_density()`` function within the ``settings()`` function. There is more information about this on the ``settings()`` reference page.

Underlying Java method: `pixelDensity <https://processing.org/reference/pixelDensity_.html>`_

Syntax
======

.. code:: python

    pixel_density(density: int) -> None

Parameters
==========

* **density**: `int` - 1 or 2


Updated on January 01, 1970 00:00:00am UTC

