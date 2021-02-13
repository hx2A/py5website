.. title: display_width
.. slug: display_width
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 display_width documentation
.. type: text

System variable that stores the width of the entire screen display.

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

    def settings():
        py5.size(py5.display_width, py5.display_height)


    def setup():
        py5.line(0, 0, py5.width, py5.height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

System variable that stores the width of the entire screen display. This is used to run a full-screen program on any display size.

Underlying Java field: displayWidth


Updated on February 13, 2021 18:02:35pm UTC

