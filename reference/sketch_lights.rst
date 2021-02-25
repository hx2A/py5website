.. title: lights()
.. slug: lights
.. date: 2021-02-25 18:37:48 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 lights() documentation
.. type: text

Sets the default ambient light, directional light, falloff, and specular values.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lights_0.png
    :alt: example picture for lights()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.no_stroke()
        # sets the default ambient
        # and directional light
        py5.lights()
        py5.translate(20, 50, 0)
        py5.sphere(30)
        py5.translate(60, 0, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_lights_1.png
    :alt: example picture for lights()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(100, 100, py5.P3D)


    def setup():
        py5.background(0)
        py5.no_stroke()


    def draw():
        # include lights() at the beginning
        # of draw() to keep them persistent
        py5.lights()
        py5.translate(20, 50, 0)
        py5.sphere(30)
        py5.translate(60, 0, 0)
        py5.sphere(30)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the default ambient light, directional light, falloff, and specular values. The defaults are ``ambientLight(128, 128, 128)`` and ``directionalLight(128, 128, 128, 0, 0, -1)``, ``lightFalloff(1, 0, 0)``, and ``lightSpecular(0, 0, 0)``. Lights need to be included in the ``draw()`` to remain persistent in a looping program. Placing them in the ``setup()`` of a looping program will cause them to only have an effect the first time through the loop.

Underlying Java method: `lights <https://processing.org/reference/lights_.html>`_

Syntax
======

.. code:: python

    lights() -> None

Updated on February 25, 2021 18:37:48pm UTC

