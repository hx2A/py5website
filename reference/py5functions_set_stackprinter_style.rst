.. title: set_stackprinter_style()
.. slug: set_stackprinter_style
.. date: 2021-04-08 15:31:29 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set_stackprinter_style() documentation
.. type: text

Set the formatting style for py5's stack traces.

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
    py5.set_stackprinter_style('lightbg')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Set the formatting style for py5's stack traces. Py5 uses the Python library stackprinter to show exception stack traces. The stackprinter library supports various color styles. By default py5 will use ``'plaintext'``, which does not use color. Alternative styles using color are ``'darkbg'``, ``'darkbg2'``, ``'darkbg3'``, ``'lightbg'``, ``'lightbg2'``, and ``'lightbg3'``.

Syntax
======

.. code:: python

    set_stackprinter_style(style: str) -> None

Parameters
==========

* **style**: `str` - name of stackprinter style


Updated on April 08, 2021 15:31:29pm UTC

