.. title: Py5Shape.get_name()
.. slug: py5shape_get_name
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_name() documentation
.. type: text

Get the name assigned to a Py5Shape object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_name_0.png
    :alt: example picture for get_name()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        us_map = py5.load_shape("us_map.svg")
        for child in us_map.get_children():
            py5.println(child.get_name())

        py5.background(192)
        py5.scale(0.1)
        py5.translate(25, 225)
        py5.shape(us_map, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the name assigned to a Py5Shape object. Will return ``None`` if the object has no name.

Underlying Java method: PShape.getName

Syntax
======

.. code:: python

    get_name() -> str

Updated on July 06, 2021 22:46:12pm UTC

