.. title: pmouse_x
.. slug: pmouse_x
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 pmouse_x documentation
.. type: text

The system variable ``pmouse_x`` always contains the horizontal position of the mouse in the frame previous to the current frame.

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
        py5.background(204)
        py5.line(py5.mouse_x, 20, py5.pmouse_x, 80)
        print(py5.mouse_x + " : " + py5.pmouse_x)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The system variable ``pmouse_x`` always contains the horizontal position of the mouse in the frame previous to the current frame.

You may find that ``pmouse_x`` and ``pmouse_y`` have different values when referenced inside of ``draw()`` and inside of mouse events like ``mouse_pressed()`` and ``mouse_moved()``. Inside ``draw()``, ``pmouse_x`` and ``pmouse_y`` update only once per frame (once per trip through the ``draw()`` loop). But inside mouse events, they update each time the event is called. If these values weren't updated immediately during mouse events, then the mouse position would be read only once per frame, resulting in slight delays and choppy interaction. If the mouse variables were always updated multiple times per frame, then something like ``line(pmouse_x, pmouse_y, mouse_x, mouse_y)`` inside ``draw()`` would have lots of gaps, because ``pmouse_x`` may have changed several times in between the calls to ``line()``.
If you want values relative to the previous frame, use ``pmouse_x`` and ``pmouse_y`` inside ``draw()``. If you want continuous response, use ``pmouse_x`` and ``pmouse_y`` inside the mouse event functions.

Underlying Java field: `pmouseX <https://processing.org/reference/pmouseX.html>`_


Updated on February 13, 2021 18:02:35pm UTC

