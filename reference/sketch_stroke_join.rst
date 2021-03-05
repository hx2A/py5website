.. title: stroke_join()
.. slug: stroke_join
.. date: 2021-03-05 15:24:25 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 stroke_join() documentation
.. type: text

Sets the style of the joints which connect line segments.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_join_0.png
    :alt: example picture for stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke_weight(10.0)
        py5.stroke_join(py5.MITER)
        py5.begin_shape()
        py5.vertex(35, 20)
        py5.vertex(65, 50)
        py5.vertex(35, 80)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_join_1.png
    :alt: example picture for stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke_weight(10.0)
        py5.stroke_join(py5.BEVEL)
        py5.begin_shape()
        py5.vertex(35, 20)
        py5.vertex(65, 50)
        py5.vertex(35, 80)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_stroke_join_2.png
    :alt: example picture for stroke_join()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_fill()
        py5.stroke_weight(10.0)
        py5.stroke_join(py5.ROUND)
        py5.begin_shape()
        py5.vertex(35, 20)
        py5.vertex(65, 50)
        py5.vertex(35, 80)
        py5.end_shape()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the style of the joints which connect line segments. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters ``MITER``, ``BEVEL``, and ``ROUND``. The default joint is ``MITER``.

Underlying Java method: `strokeJoin <https://processing.org/reference/strokeJoin_.html>`_

Syntax
======

.. code:: python

    stroke_join(join: int, /) -> None

Parameters
==========

* **join**: `int` - either MITER, BEVEL, ROUND


Updated on March 05, 2021 15:24:25pm UTC

