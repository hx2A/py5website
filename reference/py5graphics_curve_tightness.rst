.. title: Py5Graphics.curve_tightness()
.. slug: py5graphics_curve_tightness
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.curve_tightness() documentation
.. type: text

Modifies the quality of forms created with :doc:`py5graphics_curve` and :doc:`py5graphics_curve_vertex`.

Description
===========

Modifies the quality of forms created with :doc:`py5graphics_curve` and :doc:`py5graphics_curve_vertex`. The parameter ``tightness`` determines how the curve fits to the vertex points. The value 0.0 is the default value for ``tightness`` (this value defines the curves to be Catmull-Rom splines) and the value 1.0 connects all the points with straight lines. Values within the range -5.0 and 5.0 will deform the curves but will leave them recognizable and as values increase in magnitude, they will continue to deform.

This method is the same as :doc:`curve_tightness` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`curve_tightness`.

Underlying Java method: PGraphics.curveTightness

Syntax
======

.. code:: python

    curve_tightness(tightness: float, /) -> None

Parameters
==========

* **tightness**: `float` - amount of deformation from the original vertices


Updated on May 04, 2021 20:06:05pm UTC

