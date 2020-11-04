.. title: text_leading()
.. slug: sketch_text_leading
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_leading() documentation
.. type: text

Sets the spacing between lines of text in units of pixels.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_leading_0.png
    :alt: example picture for text_leading()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # text to display. the "\n" is a "new line" character
    lines = "L1\nL2\nL3"
    text_size(12)
    fill(0)  # set fill to black

    text_leading(10)  # set leading to 10
    text(lines, 10, 25)

    text_leading(20)  # set leading to 20
    text(lines, 40, 25)

    text_leading(30)  # set leading to 30
    text(lines, 70, 25)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the spacing between lines of text in units of pixels. This setting will be used in all subsequent calls to the ``text()`` function.  Note, however, that the leading is reset by ``text_size()``. For example, if the leading is set to 20 with ``text_leading(20)``, then if ``text_size(48)`` is run at a later point, the leading will be reset to the default for the text size of 48.

Underlying Java method: `textLeading <https://processing.org/reference/textLeading_.html>`_

Syntax
======

.. code:: python

    text_leading(leading: float) -> None

Parameters
==========

* **leading**: `float` - the size in pixels for spacing between lines


Updated on November 04, 2020 20:45:44pm UTC

