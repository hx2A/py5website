.. title: text_mode()
.. slug: text_mode
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_mode() documentation
.. type: text

Sets the way text draws to the screen, either as texture maps or as vector geometry.

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
        py5.size(500, 500, py5.PDF, "TypeDemo.pdf")
        py5.text_mode(py5.SHAPE)
        py5.text_size(180)


    def draw():
        py5.text("ABC", 75, 350)
        py5.exit_sketch()  # quit the program

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the way text draws to the screen, either as texture maps or as vector geometry. The default ``text_mode(MODEL)``, uses textures to render the fonts. The ``text_mode(SHAPE)`` mode draws text using the glyph outlines of individual characters rather than as textures. This mode is only supported with the ``PDF`` and ``P3D`` renderer settings. With the ``PDF`` renderer, you must call ``text_mode(SHAPE)`` before any other drawing occurs. If the outlines are not available, then ``text_mode(SHAPE)`` will be ignored and ``text_mode(MODEL)`` will be used instead.

The ``text_mode(SHAPE)`` option in ``P3D`` can be combined with :doc:`begin_raw` to write vector-accurate text to 2D and 3D output files, for instance ``DXF`` or ``PDF``. The ``SHAPE`` mode is not currently optimized for ``P3D``, so if recording shape data, use ``text_mode(MODEL)`` until you're ready to capture the geometry with :doc:`begin_raw`.

Underlying Java method: `textMode <https://processing.org/reference/textMode_.html>`_

Syntax
======

.. code:: python

    text_mode(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - either MODEL or SHAPE


Updated on June 28, 2021 15:16:14pm UTC

