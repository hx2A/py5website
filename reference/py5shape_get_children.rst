.. title: get_children()
.. slug: py5shape_get_children
.. date: 2021-04-15 21:00:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_children() documentation
.. type: text

Get the children of a Py5Shape object as a list of Py5Shape objects.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_children_0.png
    :alt: example picture for get_children()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        us_map = py5.load_shape("us_map.svg")
        for child in us_map.get_children():
            print(child.get_name())

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

Get the children of a Py5Shape object as a list of Py5Shape objects. When Processing loads shape objects, it may create a hierarchy of Py5Shapes, depending on the organization of the source data file. This method will retrieve the list of Py5Shapes that are the child objects to a given object.

Underlying Java method: PShape.getChildren

Syntax
======

.. code:: python

    get_children() -> List[Py5Shape]

Updated on April 15, 2021 21:00:57pm UTC

