.. title: no_cursor()
.. slug: no_cursor
.. date: 2021-02-27 02:51:56 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 no_cursor() documentation
.. type: text

Hides the cursor from view.

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

    # press the mouse to hide the cursor
    def draw():
        if py5.is_mouse_pressed:
            py5.no_cursor()
        else:
            py5.cursor(py5.HAND)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Hides the cursor from view. Will not work when running the program in full screen (Present) mode.

Underlying Java method: `noCursor <https://processing.org/reference/noCursor_.html>`_

Syntax
======

.. code:: python

    no_cursor() -> None

Updated on February 27, 2021 02:51:56am UTC

