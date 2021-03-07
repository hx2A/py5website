.. title: get_current_sketch()
.. slug: get_current_sketch
.. date: 2021-03-07 16:29:38 UTC+00:00
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
    py5.run_sketch(block=False)
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

Updated on March 07, 2021 16:29:38pm UTC

