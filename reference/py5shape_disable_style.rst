.. title: disable_style()
.. slug: py5shape_disable_style
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 disable_style() documentation
.. type: text

Disables the shape's style data and uses Processing's current styles.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_disable_style_0.png
    :alt: example picture for disable_style()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        # the file "bot.svg" must be in the data folder
        # of the current sketch to load successfully
        s = load_shape("bot.svg")


    def draw():
        s.disable_style()
        shape(s, -30, 10, 80, 80)
        s.enable_style()
        shape(s, 50, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Disables the shape's style data and uses Processing's current styles. Styles include attributes such as colors, stroke weight, and stroke joints.

Syntax
======

.. code:: python

    disable_style() -> None

Updated on November 03, 2020 22:19:57pm UTC

