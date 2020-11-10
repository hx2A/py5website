.. title: point_light()
.. slug: point_light
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 point_light() documentation
.. type: text

Adds a point light.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_point_light_0.png
    :alt: example picture for point_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    point_light(51, 102, 126, 35, 40, 36)
    translate(80, 50, 0)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Adds a point light. Lights need to be included in the ``draw()`` to remain persistent in a looping program. Placing them in the ``setup()`` of a looping program will cause them to only have an effect the first time through the loop. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The ``x``, ``y``, and ``z`` parameters set the position of the light.

Underlying Java method: `pointLight <https://processing.org/reference/pointLight_.html>`_

Syntax
======

.. code:: python

    point_light(v1: float, v2: float, v3: float, x: float, y: float, z: float) -> None

Parameters
==========

* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)
* **x**: `float` - x-coordinate of the light
* **y**: `float` - y-coordinate of the light
* **z**: `float` - z-coordinate of the light


Updated on November 10, 2020 15:41:45pm UTC

