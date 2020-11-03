.. title: get_child_count()
.. slug: py5shape_get_child_count
.. date: 2020-11-03 22:19:57 UTC+00:00
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
        size(100, 100)
        states = load_shape("tristate.svg")
        count = states.get_child_count()
        print(count)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Returns the number of children within the PShape.

Syntax
======

.. code:: python

    get_child_count() -> int

Updated on November 03, 2020 22:19:57pm UTC

