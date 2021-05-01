.. title: py5_tools.is_jvm_running()
.. slug: is_jvm_running
.. date: 2021-05-01 21:00:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 py5_tools.is_jvm_running() documentation
.. type: text

Determine if the Java Virtual Machine (JVM) is or is not running.

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

    # this will be False
    print(py5_tools.is_jvm_running())

    import py5

    # now it will be True
    print(py5_tools.is_jvm_running())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Determine if the Java Virtual Machine (JVM) is or is not running. When the py5 library is imported it will start the JVM.  Therefore this will be ``False`` before ``import py5`` is executed and ``True`` afterwards. It should continue to always be ``True`` unless somewhere there is some Java code that calls ``System.exit()``. Calling ``System.exit()`` is not recommended. If for some reason the JVM crashes (perhaps through a segmentation fault), the JVM will no longer be running, but that crash will most likely also terminate the Python interpreter.

Syntax
======

.. code:: python

    is_jvm_running() -> bool

Updated on May 01, 2021 21:00:05pm UTC

