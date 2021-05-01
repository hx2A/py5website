.. title: py5_tools.add_classpath()
.. slug: add_classpath
.. date: 2021-05-01 21:00:05 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 py5_tools.add_classpath() documentation
.. type: text

Add a Java jar file to the classpath.

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

    print(py5_tools.get_classpath())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Add a Java jar file to the classpath. The path to the file can be absolute or relative.

After the JVM has started, the classpath cannot be changed. This function will throw a ``RuntimeError`` if it is called after the JVM has already started. Use :doc:`is_jvm_running` to first determine if the JVM is running.

Syntax
======

.. code:: python

    add_classpath(classpath: Union[Path, str]) -> None

Parameters
==========

* **classpath**: `Union[Path, str]` - path to Java jar file


Updated on May 01, 2021 21:00:05pm UTC

