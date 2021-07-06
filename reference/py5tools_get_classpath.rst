.. title: py5_tools.get_classpath()
.. slug: get_classpath
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 py5_tools.get_classpath() documentation
.. type: text

Get the Java classpath.

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

    py5_tools.add_jars('path/to/project_jars')
    py5_tools.add_classpath('path/to/jar/file/java_code.jar')

    import py5

    py5.println(py5_tools.get_classpath())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the Java classpath. If the JVM has not yet started, this will be the classpath the JVM will use when it does start. It will also be possible to change that classpath with :doc:`add_classpath` and :doc:`add_jars`. After the JVM has started, the classpath cannot be changed and the aformentioned functions would throw a ``RuntimeError``. Use :doc:`is_jvm_running` to first determine if the JVM is running.

Syntax
======

.. code:: python

    get_classpath() -> str

Updated on July 06, 2021 22:46:12pm UTC

