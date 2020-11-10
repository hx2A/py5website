.. title: light_falloff()
.. slug: light_falloff
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 light_falloff() documentation
.. type: text

Sets the falloff rates for point lights, spot lights, and ambient lights.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_light_falloff_0.png
    :alt: example picture for light_falloff()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    size(100, 100, P3D)
    no_stroke()
    background(0)
    light_falloff(1.0, 0.001, 0.0)
    point_light(150, 250, 150, 50, 50, 50)
    begin_shape()
    vertex(0, 0, 0)
    vertex(100, 0, -100)
    vertex(100, 100, -100)
    vertex(0, 100, 0)
    end_shape(CLOSE)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the falloff rates for point lights, spot lights, and ambient lights. Like ``fill()``, it affects only the elements which are created after it in the code. The default value is ``light_falloff(1.0, 0.0, 0.0)``, and the parameters are used to calculate the falloff with the following equation:

d = distance from light position to vertex position
falloff = 1 / (CONSTANT + d * LINEAR + (d*d) * QUADRATIC)

Thinking about an ambient light with a falloff can be tricky. If you want a region of your scene to be lit ambiently with one color and another region to be lit ambiently with another color, you could use an ambient light with location and falloff. You can think of it as a point light that doesn't care which direction a surface is facing.

Underlying Java method: `lightFalloff <https://processing.org/reference/lightFalloff_.html>`_

Syntax
======

.. code:: python

    light_falloff(constant: float, linear: float, quadratic: float) -> None

Parameters
==========

* **constant**: `float` - constant value or determining falloff
* **linear**: `float` - linear value for determining falloff
* **quadratic**: `float` - quadratic value for determining falloff


Updated on January 01, 1970 00:00:00am UTC

