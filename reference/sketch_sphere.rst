.. title: sphere()
.. slug: sphere
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 sphere() documentation
.. type: text

A sphere is a hollow ball made from tessellated triangles.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_sphere_0.png
    :alt: example picture for sphere()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.lights()
        py5.translate(58, 48, 0)
        py5.sphere(28)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

A sphere is a hollow ball made from tessellated triangles.

Underlying Java method: `sphere <https://processing.org/reference/sphere_.html>`_

Syntax
======

.. code:: python

    sphere(r: float, /) -> None

Parameters
==========

* **r**: `float` - the radius of the sphere


Updated on February 13, 2021 18:02:35pm UTC

