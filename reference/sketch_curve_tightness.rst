.. title: curve_tightness()
.. slug: curve_tightness
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 curve_tightness() documentation
.. type: text

Modifies the quality of forms created with ``curve()`` and ``curve_vertex()``.

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

    # move the mouse left and right to see the curve change

    def setup():
        size(100, 100)
        no_fill()


    def draw():
        background(204)
        t = map(mouse_x, 0, width, -5, 5)
        curve_tightness(t)
        begin_shape()
        curve_vertex(10, 26)
        curve_vertex(10, 26)
        curve_vertex(83, 24)
        curve_vertex(83, 61)
        curve_vertex(25, 65)
        curve_vertex(25, 65)
        end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Modifies the quality of forms created with ``curve()`` and ``curve_vertex()``. The parameter ``tightness`` determines how the curve fits to the vertex points. The value 0.0 is the default value for ``tightness`` (this value defines the curves to be Catmull-Rom splines) and the value 1.0 connects all the points with straight lines. Values within the range -5.0 and 5.0 will deform the curves but will leave them recognizable and as values increase in magnitude, they will continue to deform.

Underlying Java method: `curveTightness <https://processing.org/reference/curveTightness_.html>`_

Syntax
======

.. code:: python

    curve_tightness(tightness: float, /) -> None

Parameters
==========

* **tightness**: `float` - amount of deformation from the original vertices


Updated on November 24, 2020 21:22:32pm UTC

