.. title: Py5Shape.get_child_count()
.. slug: py5shape_get_child_count
.. date: 2021-05-01 20:51:42 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shape.get_child_count() documentation
.. type: text

Returns the number of children within the ``Py5Shape`` object.

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
        us_map = py5.load_shape("us_map.svg")
        count = us_map.get_child_count()
        print(count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns the number of children within the ``Py5Shape`` object.

Underlying Java method: `PShape.getChildCount <https://processing.org/reference/PShape_getChildCount_.html>`_

Syntax
======

.. code:: python

    get_child_count() -> int

Updated on May 01, 2021 20:51:42pm UTC

