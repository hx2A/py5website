.. title: Py5Graphics.image_mode()
.. slug: py5graphics_image_mode
.. date: 2021-05-06 16:39:27 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.image_mode() documentation
.. type: text

Modifies the location from which images are drawn by changing the way in which parameters given to :doc:`py5graphics_image` are intepreted.

Description
===========

Modifies the location from which images are drawn by changing the way in which parameters given to :doc:`py5graphics_image` are intepreted.

The default mode is ``image_mode(CORNER)``, which interprets the second and third parameters of :doc:`py5graphics_image` as the upper-left corner of the image. If two additional parameters are specified, they are used to set the image's width and height.

``image_mode(CORNERS)`` interprets the second and third parameters of :doc:`py5graphics_image` as the location of one corner, and the fourth and fifth parameters as the opposite corner.

``image_mode(CENTER)`` interprets the second and third parameters of :doc:`py5graphics_image` as the image's center point. If two additional parameters are specified, they are used to set the image's width and height.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

This method is the same as :doc:`image_mode` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`image_mode`.

Underlying Java method: PGraphics.imageMode

Syntax
======

.. code:: python

    image_mode(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - either CORNER, CORNERS, or CENTER


Updated on May 06, 2021 16:39:27pm UTC

