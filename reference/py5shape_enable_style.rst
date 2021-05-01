.. title: Py5Shape.enable_style()
.. slug: py5shape_enable_style
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.enable_style() documentation
.. type: text

Enables the shape's style data and ignores py5's current styles.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_enable_style_0.png
    :alt: example picture for enable_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = py5.load_shape("bot.svg")


    def draw():
        s.disable_style()
        py5.shape(s, -30, 10, 80, 80)
        s.enable_style()
        py5.shape(s, 50, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Enables the shape's style data and ignores py5's current styles. Styles include attributes such as colors, stroke weight, and stroke joints.

Underlying Java method: `PShape.enableStyle <https://processing.org/reference/PShape_enableStyle_.html>`_

Syntax
======

.. code:: python

    enable_style() -> None

Updated on May 01, 2021 20:51:42pm UTC

