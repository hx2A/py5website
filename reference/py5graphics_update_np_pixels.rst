.. title: Py5Graphics.update_np_pixels()
.. slug: py5graphics_update_np_pixels
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Graphics.update_np_pixels() documentation
.. type: text

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_np_pixels` array.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Graphics_update_np_pixels_0.png
    :alt: example picture for update_np_pixels()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        g = py5.create_graphics(80, 80)
        g.begin_draw()
        g.background(255)
        g.rect(10, 10, 60, 60)
        g.load_np_pixels()
        g.np_pixels[:, 40:, 1:] = [255, 0, 0]
        g.update_np_pixels()
        g.end_draw()
        py5.image(g, 10, 10)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Updates the Py5Graphics drawing surface with the data in the :doc:`py5graphics_np_pixels` array. Use in conjunction with :doc:`py5graphics_load_np_pixels`. If you're only reading pixels from the array, there's no need to call ``update_np_pixels()`` — updating is only necessary to apply changes. Working with :doc:`py5graphics_np_pixels` can only be done between calls to :doc:`py5graphics_begin_draw` and :doc:`py5graphics_end_draw`.

The ``update_np_pixels()`` method is similar to :doc:`py5graphics_update_pixels` in that ``update_np_pixels()`` must be called after modifying :doc:`py5graphics_np_pixels` just as :doc:`py5graphics_update_pixels` must be called after modifying :doc:`py5graphics_pixels`.

This method is the same as :doc:`update_np_pixels` but linked to a ``Py5Graphics`` object.

Syntax
======

.. code:: python

    update_np_pixels() -> None

Updated on July 06, 2021 22:46:12pm UTC

