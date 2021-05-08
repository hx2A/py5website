.. title: Py5Graphics.texture_wrap()
.. slug: py5graphics_texture_wrap
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.texture_wrap() documentation
.. type: text

Defines if textures repeat or draw once within a texture map.

Description
===========

Defines if textures repeat or draw once within a texture map. The two parameters are ``CLAMP`` (the default behavior) and ``REPEAT``. This function only works with the ``P2D`` and ``P3D`` renderers.

This method is the same as :doc:`texture_wrap` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`texture_wrap`.

Underlying Java method: PGraphics.textureWrap

Syntax
======

.. code:: python

    texture_wrap(wrap: int, /) -> None

Parameters
==========

* **wrap**: `int` - Either CLAMP (default) or REPEAT


Updated on May 04, 2021 20:06:05pm UTC

