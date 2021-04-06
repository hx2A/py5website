.. title: java_platform
.. slug: java_platform
.. date: 2021-04-06 18:47:56 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 java_platform documentation
.. type: text

Version of Java currently being used by py5.

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
        print(py5.java_platform)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Version of Java currently being used by py5. Internally the py5 library is using the Processing Java libraries to provide functionality. Those libraries run in a Java Virtual Machine. This field provides the Java platform number for that Virtual Machine.

Underlying Java field: javaPlatform


Updated on April 06, 2021 18:47:56pm UTC

