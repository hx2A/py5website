.. title: load_font()
.. slug: load_font
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_font() documentation
.. type: text

Loads a .vlw formatted font into a ``Py5Font`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_font_0.png
    :alt: example picture for load_font()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # the font must be located in the sketch's
    # "data" directory to load successfully
    font = load_font("LetterGothicStd-32.vlw")
    text_font(font, 32)
    text("word", 10, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Loads a .vlw formatted font into a ``Py5Font`` object. Create a .vlw font by selecting "Create Font..." from the Tools menu. This tool creates a texture for each alphanumeric character and then adds them as a .vlw file to the current sketch's data folder. Because the letters are defined as textures (and not vector data) the size at which the fonts are created must be considered in relation to the size at which they are drawn. For example, load a 32pt font if the sketch displays the font at 32 pixels or smaller. Conversely, if a 12pt font is loaded and displayed at 48pts, the letters will be distorted because the program will be stretching a small graphic to a large size.

Like ``load_image()`` and other functions that load data, the ``load_font()`` function should not be used inside ``draw()``, because it will slow down the sketch considerably, as the font will be re-loaded from the disk (or network) on each frame. It's recommended to load files inside ``setup()``

To load correctly, fonts must be located in the "data" folder of the current sketch. Alternatively, the file maybe be loaded from anywhere on the local computer using an absolute path (something that starts with / on Unix and Linux, or a drive letter on Windows), or the filename parameter can be a URL for a file found on a network.

If the file is not available or an error occurs, ``None`` will be returned and an error message will be printed to the console. The error message does not halt the program, however the null value may cause a NullPointerException if your code does not check whether the value returned is null.

Use ``create_font()`` (instead of ``load_font()``) to enable vector data to be used with the default renderer setting. This can be helpful when many font sizes are needed, or when using any renderer based on the default renderer, such as the PDF library.

Underlying Java method: `loadFont <https://processing.org/reference/loadFont_.html>`_

Syntax
======

.. code:: python

    load_font(filename: str) -> Py5Font

Parameters
==========

* **filename**: `str` - name of the font to load


Updated on January 01, 1970 00:00:00am UTC

