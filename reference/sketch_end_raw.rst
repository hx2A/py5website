.. title: end_raw()
.. slug: end_raw
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_raw() documentation
.. type: text

Complement to ``begin_raw()``; they must always be used together.

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
        begin_raw(PDF, "raw.pdf")


    def draw():
        line(pmouse_x, pmouse_y, mouse_x, mouse_y)


    def key_pressed():
        if key == ' ':
            end_raw()
            exit()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Complement to ``begin_raw()``; they must always be used together. See the ``begin_raw()`` reference for details.

Underlying Java method: `endRaw <https://processing.org/reference/endRaw_.html>`_

Syntax
======

.. code:: python

    end_raw() -> None

Updated on November 10, 2020 15:41:45pm UTC

