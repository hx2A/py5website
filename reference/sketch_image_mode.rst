.. title: image_mode()
.. slug: image_mode
.. date: 2021-03-04 20:16:29 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 image_mode() documentation
.. type: text

Modifies the location from which images are drawn by changing the way in which parameters given to :doc:`image` are intepreted.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_image_mode_0.png
    :alt: example picture for image_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img
        img = py5.load_image("laDefense.jpg")


    def draw():
        py5.image_mode(py5.CORNER)
        py5.image(img, 10, 10, 50, 50)  # draw image using CORNER mode

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_image_mode_1.png
    :alt: example picture for image_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img
        img = py5.load_image("laDefense.jpg")


    def draw():
        py5.image_mode(py5.CORNERS)
        py5.image(img, 10, 10, 90, 40)  # draw image using CORNERS mode

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_image_mode_2.png
    :alt: example picture for image_mode()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global img
        img = py5.load_image("laDefense.jpg")


    def draw():
        py5.image_mode(py5.CENTER)
        py5.image(img, 50, 50, 80, 80)  # draw image using CENTER mode

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Modifies the location from which images are drawn by changing the way in which parameters given to :doc:`image` are intepreted.

The default mode is ``image_mode(CORNER)``, which interprets the second and third parameters of :doc:`image` as the upper-left corner of the image. If two additional parameters are specified, they are used to set the image's width and height.

``image_mode(CORNERS)`` interprets the second and third parameters of :doc:`image` as the  location of one corner, and the fourth and fifth parameters as the opposite corner.

``image_mode(CENTER)`` interprets the second and third parameters of :doc:`image` as the image's center point. If two additional parameters are specified, they are used to set the image's width and height.

The parameter must be written in ALL CAPS because Python is a case-sensitive language.

Underlying Java method: `imageMode <https://processing.org/reference/imageMode_.html>`_

Syntax
======

.. code:: python

    image_mode(mode: int, /) -> None

Parameters
==========

* **mode**: `int` - either CORNER, CORNERS, or CENTER


Updated on March 04, 2021 20:16:29pm UTC

