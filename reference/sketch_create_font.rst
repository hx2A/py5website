.. title: create_font()
.. slug: create_font
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_font() documentation
.. type: text

Dynamically converts a font to the format used by Processing from a .ttf or .otf file inside the sketch's "data" folder or a font that's installed elsewhere on the computer.

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

    def setup():
        global my_font
        size(200, 200)
        # uncomment the following two lines to see the available fonts
        # string[] font_list = Py5Font.list()
        # print_array(font_list)
        my_font = create_font("Georgia", 32)
        text_font(my_font)
        text_align(CENTER, CENTER)
        text("!@#$%", width//2, height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Dynamically converts a font to the format used by Processing from a .ttf or .otf file inside the sketch's "data" folder or a font that's installed elsewhere on the computer. If you want to use a font installed on your computer, use the ``Py5Font.list()`` method to first determine the names for the fonts recognized by the computer and are compatible with this function. Not all fonts can be used and some might work with one operating system and not others. When sharing a sketch with other people or posting it on the web, you may need to include a .ttf or .otf version of your font in the data directory of the sketch because other people might not have the font installed on their computer. Only fonts that can legally be distributed should be included with a sketch.

The ``size`` parameter states the font size you want to generate. The ``smooth`` parameter specifies if the font should be antialiased or not. The ``charset`` parameter is an array of chars that specifies the characters to generate.

This function allows Processing to work with the font natively in the default renderer, so the letters are defined by vector geometry and are rendered quickly. In the ``P2D`` and ``P3D`` renderers, the function sets the project to render the font as a series of small textures. For instance, when using the default renderer, the actual native version of the font will be employed by the sketch, improving drawing quality and performance. With the ``P2D`` and ``P3D`` renderers, the bitmapped version will be used to improve speed and appearance, but the results are poor when exporting if the sketch does not include the .otf or .ttf file, and the requested font is not available on the machine running the sketch.

Underlying Java method: `createFont <https://processing.org/reference/createFont_.html>`_

Syntax
======

.. code:: python

    create_font(name: str, size: float) -> Py5Font
    create_font(name: str, size: float, smooth: bool) -> Py5Font
    create_font(name: str, size: float, smooth: bool, charset: List[chr]) -> Py5Font

Parameters
==========

* **charset**: `List[chr]` - array containing characters to be generated
* **name**: `str` - name of the font to load
* **size**: `float` - point size of the font
* **smooth**: `bool` - true for an antialiased font, false for aliased


Updated on January 01, 1970 00:00:00am UTC

