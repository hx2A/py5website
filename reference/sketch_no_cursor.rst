.. title: no_cursor()
.. slug: no_cursor
.. date: 2020-11-10 15:41:45 UTC+00:00
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
        if mouse_pressed:
            no_cursor()
        else:
            cursor(HAND)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Hides the cursor from view. Will not work when running the program in a web browser or in full screen (Present) mode.

Underlying Java method: `noCursor <https://processing.org/reference/noCursor_.html>`_

Syntax
======

.. code:: python

    no_cursor() -> None

Updated on November 10, 2020 15:41:45pm UTC

