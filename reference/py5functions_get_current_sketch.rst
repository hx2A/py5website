.. title: get_current_sketch()
.. slug: get_current_sketch
.. date: 2021-02-10 15:43:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_current_sketch() documentation
.. type: text

Get the py5 module's current ``Sketch`` instance.

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

    sketch = py5.get_current_sketch()
    assert sketch.is_ready
    py5.run_sketch()
    assert sketch.is_running
    py5.exit_sketch()
    assert sketch.is_dead

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the py5 module's current ``Sketch`` instance.

When coding py5 in module mode, a Sketch instance is created on your behalf that is referenced within the py5 module itself. That Sketch is called the "current sketch." Use this method to access that Sketch instance directly.

Syntax
======

.. code:: python

    get_current_sketch() -> Sketch

Updated on February 10, 2021 15:43:05pm UTC

