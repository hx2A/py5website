.. title: get_child_count()
.. slug: py5shape_get_child_count
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_child_count() documentation
.. type: text

Returns the number of children within the PShape.

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
        global states
        states = py5.load_shape("tristate.svg")
        count = states.get_child_count()
        print(count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns the number of children within the PShape.

Underlying Java method: `PShape.getChildCount <https://processing.org/reference/PShape_getChildCount_.html>`_

Syntax
======

.. code:: python

    get_child_count() -> int

Updated on February 13, 2021 18:02:35pm UTC

