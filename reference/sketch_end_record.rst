.. title: end_record()
.. slug: sketch_end_record
.. date: 2020-11-03 22:19:57 UTC+00:00
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

Syntax
======

.. code:: python

    end_record() -> None

Updated on November 03, 2020 22:19:57pm UTC

