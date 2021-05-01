.. title: Py5Shape.get_kind()
.. slug: py5shape_get_kind
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_kind() documentation
.. type: text

Get the Py5Shape object's "kind" number.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_kind_0.png
    :alt: example picture for get_kind()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # this is just a subset of the possible values
    PY5SHAPE_KIND_VALS = {py5.Py5Shape.GROUP: 'GROUP',
                          py5.Py5Shape.ELLIPSE: 'ELLIPSE'}


    def setup():
        s = py5.load_shape("bot.svg")
        for child in s.get_children():
            print(PY5SHAPE_KIND_VALS[child.get_kind()])

        py5.background(192)
        py5.scale(0.25)
        py5.shape(s, py5.width//2, py5.height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the Py5Shape object's "kind" number.

Underlying Java method: PShape.getKind

Syntax
======

.. code:: python

    get_kind() -> int

Updated on May 01, 2021 20:51:42pm UTC

