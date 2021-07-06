.. title: java_version_name
.. slug: java_version_name
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 java_version_name documentation
.. type: text

Version name of Java currently being used by py5.

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
        py5.println(py5.java_version_name)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Version name of Java currently being used by py5. Internally the py5 library is using the Processing Java libraries to provide functionality. Those libraries run in a Java Virtual Machine. This field provides the Java version name for that Virtual Machine.

Underlying Java field: javaVersionName


Updated on July 06, 2021 22:46:12pm UTC

