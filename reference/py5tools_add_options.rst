.. title: add_options()
.. slug: add_options
.. date: 2021-04-07 18:55:47 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 add_options() documentation
.. type: text

Provide JVM options to use when the JVM starts.

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

    import py5_tools
    py5_tools.add_options('-Xmx4096m')
    import py5

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Provide JVM options to use when the JVM starts. This is useful to set the JVM memory size, for example.

After the JVM has started, new options cannot be added. This function will throw a ``RuntimeError`` if it is called after the JVM has already started. Use :doc:`is_jvm_running` to first determine if the JVM is running.

Syntax
======

.. code:: python

    add_options(*options: List[str]) -> None

Parameters
==========

* **options**: `List[str]` - list of desired JVM options


Updated on April 07, 2021 18:55:47pm UTC

