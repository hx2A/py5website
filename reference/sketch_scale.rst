.. title: scale()
.. slug: sketch_scale
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 scale() documentation
.. type: text

Increases or decreases the size of a shape by expanding and contracting vertices.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_scale_0.png
    :alt: example picture for scale()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    rect(30, 20, 50, 50)
    scale(0.5)
    rect(30, 20, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_scale_1.png
    :alt: example picture for scale()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    rect(30, 20, 50, 50)
    scale(0.5, 1.3)
    rect(30, 20, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_scale_2.png
    :alt: example picture for scale()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # scaling in 3D requires P3D
    # as a parameter to size()
    size(100, 100, P3D)
    no_fill()
    translate(width//2+12, height//2)
    box(20, 20, 20)
    scale(2.5, 2.5, 2.5)
    box(20, 20, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Increases or decreases the size of a shape by expanding and contracting vertices. Objects always scale from their relative origin to the coordinate system. Scale values are specified as decimal percentages. For example, the function call ``scale(2.0)`` increases the dimension of a shape by 200%.

Transformations apply to everything that happens after and subsequent calls to the function multiply the effect. For example, calling ``scale(2.0)`` and then ``scale(1.5)`` is the same as ``scale(3.0)``. If ``scale()`` is called within ``draw()``, the transformation is reset when the loop begins again. Using this function with the ``z`` parameter requires using P3D as a parameter for ``size()``, as shown in the third example above. This function can be further controlled with ``push_matrix()`` and ``pop_matrix()``.

Underlying Java method: `scale <https://processing.org/reference/scale_.html>`_

Syntax
======

.. code:: python

    scale(s: float) -> None
    scale(x: float, y: float) -> None
    scale(x: float, y: float, z: float) -> None

Parameters
==========

* **s**: `float` - percentage to scale the object
* **x**: `float` - percentage to scale the object in the x-axis
* **y**: `float` - percentage to scale the object in the y-axis
* **z**: `float` - percentage to scale the object in the z-axis


Updated on November 04, 2020 20:45:44pm UTC

