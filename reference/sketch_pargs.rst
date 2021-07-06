.. title: pargs
.. slug: pargs
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pargs documentation
.. type: text

List of strings passed to the Sketch through the call to :doc:`run_sketch`.

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
        color = eval(py5.pargs[0])
        py5.background(color)

    py5.run_sketch(sketch_args=['0xFF0000'])

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

List of strings passed to the Sketch through the call to :doc:`run_sketch`. Only passing strings is allowed, but you can convert string types to something else to make this more useful.

Underlying Java field: args


Updated on July 06, 2021 22:46:12pm UTC

