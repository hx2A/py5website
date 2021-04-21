.. title: get_parent()
.. slug: py5shape_get_parent
.. date: 2021-04-21 14:25:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_parent() documentation
.. type: text

Locate a child ``Py5Shape`` object's parent ``GROUP`` ``Py5Shape`` object.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Shape_get_parent_0.png
    :alt: example picture for get_parent()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        p = py5.create_shape(py5.GROUP)
        s1 = py5.create_shape(py5.RECT, 10, 10, 35, 35)
        p.add_child(s1)
        s2 = py5.create_shape(py5.RECT, 55, 10, 35, 35)
        p.add_child(s2)
        py5.shape(s2.get_parent())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Locate a child ``Py5Shape`` object's parent ``GROUP`` ``Py5Shape`` object. This will return ``None`` if the shape has no parent, such as when the shape is the parent object or the shape is not a part of a group.

Underlying Java method: PShape.getParent

Syntax
======

.. code:: python

    get_parent() -> Py5Shape

Updated on April 21, 2021 14:25:32pm UTC

