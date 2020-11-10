.. title: text_size()
.. slug: text_size
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 text_size() documentation
.. type: text

Sets the current font size.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_text_size_0.png
    :alt: example picture for text_size()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    background(0)
    fill(255)
    text_size(26)
    text("WORD", 10, 50)
    text_size(14)
    text("WORD", 10, 70)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the current font size. This size will be used in all subsequent calls to the ``text()`` function. Font size is measured in units of pixels.

Underlying Java method: `textSize <https://processing.org/reference/textSize_.html>`_

Syntax
======

.. code:: python

    text_size(size: float) -> None

Parameters
==========

* **size**: `float` - the size of the letters in units of pixels


Updated on November 10, 2020 15:41:45pm UTC

