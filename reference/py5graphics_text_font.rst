.. title: Py5Graphics.text_font()
.. slug: py5graphics_text_font
.. date: 2021-05-04 20:06:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.text_font() documentation
.. type: text

Sets the current font that will be drawn with the :doc:`py5graphics_text` function.

Description
===========

Sets the current font that will be drawn with the :doc:`py5graphics_text` function. Fonts must be created for py5 with :doc:`create_font` or loaded with :doc:`load_font` before they can be used. The font set through ``text_font()`` will be used in all subsequent calls to the :doc:`py5graphics_text` function. If no ``size`` parameter is specified, the font size defaults to the original size (the size in which it was created with :doc:`create_font_file`) overriding any previous calls to ``text_font()`` or :doc:`py5graphics_text_size`.

When fonts are rendered as an image texture (as is the case with the ``P2D`` and ``P3D`` renderers as well as with :doc:`load_font` and vlw files), you should create fonts at the sizes that will be used most commonly. Using ``text_font()`` without the size parameter will result in the cleanest type.

This method is the same as :doc:`text_font` but linked to a ``Py5Graphics`` object. To see example code for how it can be used, see :doc:`text_font`.

Underlying Java method: PGraphics.textFont

Syntax
======

.. code:: python

    text_font(which: Py5Font, /) -> None
    text_font(which: Py5Font, size: float, /) -> None

Parameters
==========

* **size**: `float` - the size of the letters in units of pixels
* **which**: `Py5Font` - any variable of the type Py5Font


Updated on May 04, 2021 20:06:05pm UTC

