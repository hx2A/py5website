.. title: get_graphics()
.. slug: get_graphics
.. date: 2021-04-11 15:16:11 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_graphics() documentation
.. type: text

Get the :doc:`py5graphics` object used by the Sketch.

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
        py5.rect(10, 10, 50, 50)
        g = py5.get_graphics()
        print(type(g))

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the :doc:`py5graphics` object used by the Sketch. Internally, all of Processing's drawing functionality comes from interaction with PGraphics objects, and this will provide direct access to the PGraphics object used by the Sketch.

Underlying Java method: getGraphics

Syntax
======

.. code:: python

    get_graphics() -> Py5Graphics

Updated on April 11, 2021 15:16:11pm UTC

