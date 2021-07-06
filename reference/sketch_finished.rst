.. title: finished
.. slug: finished
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 finished documentation
.. type: text

Boolean variable reflecting if the Sketch has stopped permanently.

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

    import time

    def draw():
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)


    py5.run_sketch()
    py5.println('sketch has stopped:', py5.finished)
    time.sleep(10)

    py5.exit_sketch()
    py5.println('sketch has stopped:', py5.finished)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Boolean variable reflecting if the Sketch has stopped permanently.

Underlying Java field: finished


Updated on July 06, 2021 22:46:12pm UTC

