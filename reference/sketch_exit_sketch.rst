.. title: exit_sketch()
.. slug: exit_sketch
.. date: 2020-11-13 19:13:07 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 exit_sketch() documentation
.. type: text

Quits/stops/exits the program.

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

    def draw():
        line(mouse_x, mouse_y, 50, 50)


    def mouse_pressed():
        exit()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Quits/stops/exits the program. Programs without a ``draw()`` function stop automatically after the last line has run, but programs with ``draw()`` run continuously until the program is manually stopped or ``exit()`` is run.

Rather than terminating immediately, ``exit()`` will cause the sketch to exit after ``draw()`` has completed (or after ``setup()`` completes if called during the ``setup()`` function).

For Java programmers, this is *not* the same as System.``exit()``. Further, System.``exit()`` should not be used because closing out an application while ``draw()`` is running may cause a crash (particularly with P3D).

Underlying Java method: `exit <https://processing.org/reference/exit_.html>`_

Syntax
======

.. code:: python

    exit_sketch() -> None

Updated on November 13, 2020 19:13:07pm UTC

