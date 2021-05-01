.. title: Py5Shape.get_family()
.. slug: py5shape_get_family
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_family() documentation
.. type: text

Get the Py5Shape object's "family" number.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_family_0.png
    :alt: example picture for get_family()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # family will be one of these values
    SHAPE_FAMILY_VALS = {py5.Py5Shape.GROUP: 'GROUP',
                         py5.Py5Shape.PRIMITIVE: 'PRIMITIVE',
                         py5.Py5Shape.PATH: 'PATH',
                         py5.Py5Shape.GEOMETRY: 'GEOMETRY'}


    def setup():
        s = py5.load_shape("bot.svg")
        for child in s.get_children():
            print(SHAPE_FAMILY_VALS[child.get_family()])

        py5.background(192)
        py5.scale(0.25)
        py5.shape(s, py5.width//2, py5.height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the Py5Shape object's "family" number.

Underlying Java method: PShape.getFamily

Syntax
======

.. code:: python

    get_family() -> int

Updated on May 01, 2021 20:51:42pm UTC

