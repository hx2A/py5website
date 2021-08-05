.. title: Py5Shape.set_name()
.. slug: py5shape_set_name
.. date: 2021-08-02 23:44:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.set_name() documentation
.. type: text

Assign a name to a ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_set_name_0.png
    :alt: example picture for set_name()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        s = py5.create_shape(py5.GROUP)
        s1 = py5.create_shape(py5.RECT, 10, 10, 35, 35)
        s1.set_name("rectangle1")
        s.add_child(s1)
        s2 = py5.create_shape(py5.RECT, 55, 10, 35, 35)
        s2.set_name("rectangle2")
        s.add_child(s2)
        py5.shape(s)

        s_child1 = s.get_child("rectangle1")
        s_child1.set_fill("#FF0000")
        s_child2 = s.get_child("rectangle2")
        s_child2.set_fill("#00FF00")
        py5.shape(s, 0, 45)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Assign a name to a ``Py5Shape`` object. This can be used to later find the shape in a ``GROUP`` shape.

Underlying Java method: PShape.setName

Syntax
======

.. code:: python

    set_name(name: str, /) -> None

Parameters
==========

* **name**: `str` - name to be assigned to shape


Updated on August 02, 2021 23:44:12pm UTC

