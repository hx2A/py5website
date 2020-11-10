.. title: focused
.. slug: focused
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 focused documentation
.. type: text

Confirms if a Processing program is "focused," meaning that it is active and will accept mouse or keyboard input.

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

    if focused:  # or "if (focused == true)"
        ellipse(25, 25, 50, 50)
    else:
        line(0, 0, 100, 100)
        line(100, 0, 0, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Confirms if a Processing program is "focused," meaning that it is active and will accept mouse or keyboard input. This variable is "true" if it is focused and "false" if not.

Underlying Java field: `focused <https://processing.org/reference/focused.html>`_


Updated on November 10, 2020 15:41:45pm UTC

