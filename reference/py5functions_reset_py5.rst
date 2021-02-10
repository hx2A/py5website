.. title: reset_py5()
.. slug: reset_py5
.. date: 2021-02-10 15:43:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 reset_py5() documentation
.. type: text

Reset the py5 module's current ``Sketch`` instance.

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

    import py5

    assert py5.is_ready
    first_sketch = py5.get_current_sketch()
    py5.run_sketch()
    py5.exit_sketch()
    assert py5.is_dead
    py5.reset_py5()
    assert py5.is_ready
    second_sketch = py5.get_current_sketch()
    assert first_sketch is not second_sketch

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Reset the py5 module's current ``Sketch`` instance.

When coding py5 in module mode, a Sketch instance is created on your behalf that is referenced within the py5 module itself. That Sketch is called the "current sketch." If the current sketch exits, it will be in a dead state and cannot be re-run. ``reset_py5()`` will discard that exited Sketch instance and replace it with a new one in the ready state.

If ``reset_py5()`` is called when the current sketch is in the ready or running states, it will do nothing and return ``False``. If ``reset_py5()`` is called when the current sketch is in the dead state, ``reset_py5()`` will replace it and return ``True``.

Syntax
======

.. code:: python

    reset_py5() -> bool

Updated on February 10, 2021 15:43:05pm UTC

