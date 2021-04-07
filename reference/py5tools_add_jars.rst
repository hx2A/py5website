.. title: add_jars()
.. slug: add_jars
.. date: 2021-04-07 18:55:47 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 add_jars() documentation
.. type: text

Add all of the Java jar files contained in a directory and its subdirectories to the classpath.

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

Add all of the Java jar files contained in a directory and its subdirectories to the classpath. The path can be absolute or relative. If the directory does does not exist, it will be ignored.

When ``import py5`` is executed, ``add_jars('jars')`` is called for you to automatically add jar files contained in a subdirectory called jars. This is similar to functionality provided by the Processing IDE.

After the JVM has started, the classpath cannot be changed. This function will throw a ``RuntimeError`` if it is called after the JVM has already started. Use :doc:`is_jvm_running` to first determine if the JVM is running.

Syntax
======

.. code:: python

    add_jars(path: Union[Path, str]) -> None

Parameters
==========

* **path**: `Union[Path, str]` - path to directory containing jar files


Updated on April 07, 2021 18:55:47pm UTC

