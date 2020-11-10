.. title: end_record()
.. slug: end_record
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_record() documentation
.. type: text

Stops the recording process started by ``begin_record()`` and closes the file.

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
        size(400, 400)
        begin_record(PDF, "everything.pdf")


    def draw():
        ellipse(mouse_x, mouse_y, 10, 10)


    def mouse_pressed():
        end_record()
        exit()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Stops the recording process started by ``begin_record()`` and closes the file.

Underlying Java method: `endRecord <https://processing.org/reference/endRecord_.html>`_

Syntax
======

.. code:: python

    end_record() -> None

Updated on January 01, 1970 00:00:00am UTC

