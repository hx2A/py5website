.. title: end_record()
.. slug: end_record
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_record() documentation
.. type: text

Stops the recording process started by :doc:`begin_record` and closes the file.

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
        py5.size(400, 400)
        py5.begin_record(py5.PDF, "everything.pdf")


    def draw():
        py5.ellipse(py5.mouse_x, py5.mouse_y, 10, 10)


    def mouse_pressed():
        py5.end_record()
        py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Stops the recording process started by :doc:`begin_record` and closes the file.

Underlying Java method: `endRecord <https://processing.org/reference/endRecord_.html>`_

Syntax
======

.. code:: python

    end_record() -> None

Updated on June 28, 2021 15:16:14pm UTC

