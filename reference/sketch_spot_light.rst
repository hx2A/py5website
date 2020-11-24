.. title: spot_light()
.. slug: spot_light
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 spot_light() documentation
.. type: text

Adds a spot light.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_spot_light_0.png
    :alt: example picture for spot_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    background(0)
    no_stroke()
    spot_light(51, 102, 126, 80, 20, 40, -1, 0, 0, PI/2, 2)
    translate(20, 50, 0)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_spot_light_1.png
    :alt: example picture for spot_light()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    concentration = 600  # try 1 -> 10000
    background(0)
    no_stroke()
    spot_light(51, 102, 126, 50, 50, 400,
               0, 0, -1, PI/16, concentration)
    translate(80, 50, 0)
    sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Adds a spot light. Lights need to be included in the ``draw()`` to remain persistent in a looping program. Placing them in the ``setup()`` of a looping program will cause them to only have an effect the first time through the loop. The ``v1``, ``v2``, and ``v3`` parameters are interpreted as either RGB or HSB values, depending on the current color mode. The ``x``, ``y``, and ``z`` parameters specify the position of the light and ``nx``, ``ny``, ``nz`` specify the direction of light. The ``angle`` parameter affects angle of the spotlight cone, while ``concentration`` sets the bias of light focusing toward the center of that cone.

Underlying Java method: `spotLight <https://processing.org/reference/spotLight_.html>`_

Syntax
======

.. code:: python

    spot_light(v1: float, v2: float, v3: float, x: float, y: float, z: float, nx: float, ny: float, nz: float, angle: float, concentration: float, /) -> None

Parameters
==========

* **angle**: `float` - angle of the spotlight cone
* **concentration**: `float` - exponent determining the center bias of the cone
* **nx**: `float` - direction along the x axis
* **ny**: `float` - direction along the y axis
* **nz**: `float` - direction along the z axis
* **v1**: `float` - red or hue value (depending on current color mode)
* **v2**: `float` - green or saturation value (depending on current color mode)
* **v3**: `float` - blue or brightness value (depending on current color mode)
* **x**: `float` - x-coordinate of the light
* **y**: `float` - y-coordinate of the light
* **z**: `float` - z-coordinate of the light


Updated on November 24, 2020 21:22:32pm UTC

