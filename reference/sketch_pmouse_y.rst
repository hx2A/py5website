.. title: pmouse_y
.. slug: sketch_pmouse_y
.. date: 2020-11-03 22:19:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pmouse_y documentation
.. type: text

The system variable ``pmouse_y`` always contains the vertical position of the mouse in the frame previous to the current frame.

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

    # move the mouse quickly to see the difference
    # between the current and previous position
    def draw():
        background(204)
        line(20, mouse_y, 80, pmouse_y)
        print(mouse_y + " : " + pmouse_y)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The system variable ``pmouse_y`` always contains the vertical position of the mouse in the frame previous to the current frame.

For more detail on how ``pmouse_y`` is updated inside of mouse events and ``draw()``, see the reference for ``pmouse_x``.


Updated on November 03, 2020 22:19:57pm UTC

