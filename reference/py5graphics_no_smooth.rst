.. title: Py5Graphics.no_smooth()
.. slug: py5graphics_no_smooth
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.no_smooth() documentation
.. type: text

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.

Description
===========

Draws all geometry and fonts with jagged (aliased) edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.  Note that :doc:`py5graphics_smooth` is active by default, so it is necessary to call ``no_smooth()`` to disable smoothing of geometry, fonts, and images. The ``no_smooth()`` method can only be run once for a ``Py5Graphics`` object and it must be called before :doc:`py5graphics_begin_draw`.

This method is the same as :doc:`no_smooth` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`no_smooth`.

Underlying Java method: PGraphics.noSmooth

Syntax
======

.. code:: python

    no_smooth() -> None

Updated on May 06, 2021 16:39:27pm UTC

