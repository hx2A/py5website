.. title: no_tint()
.. slug: sketch_no_tint
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_tint() documentation
.. type: text

Removes the current fill value for displaying images and reverts to displaying images with their original hues.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_no_tint_0.png
    :alt: example picture for no_tint()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    img = load_image("laDefense.jpg")
    tint(0, 153, 204)  # tint blue
    image(img, 0, 0)
    no_tint()  # disable tint
    image(img, 50, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Removes the current fill value for displaying images and reverts to displaying images with their original hues.

Underlying Java method: `noTint <https://processing.org/reference/noTint_.html>`_

Syntax
======

.. code:: python

    no_tint() -> None

Updated on November 04, 2020 20:45:44pm UTC

