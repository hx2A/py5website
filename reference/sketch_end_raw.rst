.. title: end_raw()
.. slug: end_raw
.. date: 2021-02-25 16:37:22 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 end_raw() documentation
.. type: text

Complement to :doc:`begin_raw`; they must always be used together.

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
        py5.size(400, 400, py5.P2D)


    def setup():
        py5.begin_raw(py5.PDF, "raw.pdf")


    def draw():
        py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)


    def key_pressed():
        if py5.key == ' ':
            py5.end_raw()
            py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Complement to :doc:`begin_raw`; they must always be used together. See the :doc:`begin_raw` reference for details.

Underlying Java method: `endRaw <https://processing.org/reference/endRaw_.html>`_

Syntax
======

.. code:: python

    end_raw() -> None

Updated on February 25, 2021 16:37:22pm UTC

