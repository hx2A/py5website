.. title: set_name()
.. slug: py5shape_set_name
.. date: 2021-04-20 16:39:51 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_name() documentation
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
        s_child1.set_fill(py5.color(255, 0, 0))
        s_child2 = s.get_child("rectangle2")
        s_child2.set_fill(py5.color(0, 255, 0))
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


Updated on April 20, 2021 16:39:51pm UTC

