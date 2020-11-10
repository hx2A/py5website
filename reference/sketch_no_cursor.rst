.. title: no_cursor()
.. slug: no_cursor
.. date: 1970-01-01 00:00:00 UTC+00:00
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

Updated on January 01, 1970 00:00:00am UTC

