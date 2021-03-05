.. title: focused
.. slug: focused
.. date: 2021-03-05 15:12:39 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 focused documentation
.. type: text

Confirms if a py5 program is "focused," meaning that it is active and will accept mouse or keyboard input.

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
        if py5.focused:
            py5.ellipse(25, 25, 50, 50)
        else:
            py5.line(0, 0, 100, 100)
            py5.line(100, 0, 0, 100)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Confirms if a py5 program is "focused," meaning that it is active and will accept mouse or keyboard input. This variable is ``True`` if it is focused and ``False`` if not.

Underlying Java field: `focused <https://processing.org/reference/focused.html>`_


Updated on March 05, 2021 15:12:39pm UTC

