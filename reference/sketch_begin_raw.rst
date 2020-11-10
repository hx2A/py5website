.. title: begin_raw()
.. slug: begin_raw
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_raw() documentation
.. type: text

To create vectors from 3D data, use the ``begin_raw()`` and ``end_raw()`` commands.

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
        size(400, 400)
        begin_raw(PDF, "raw.pdf")


    def draw():
        line(pmouse_x, pmouse_y, mouse_x, mouse_y)


    def key_pressed():
        if key == ' ':
            end_raw()
            exit()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

To create vectors from 3D data, use the ``begin_raw()`` and ``end_raw()`` commands. These commands will grab the shape data just before it is rendered to the screen. At this stage, your entire scene is nothing but a long list of individual lines and triangles. This means that a shape created with ``sphere()`` function will be made up of hundreds of triangles, rather than a single object. Or that a multi-segment line shape (such as a curve) will be rendered as individual segments.

When using ``begin_raw()`` and ``end_raw()``, it's possible to write to either a 2D or 3D renderer. For instance, ``begin_raw()`` with the PDF library will write the geometry as flattened triangles and lines, even if recording from the ``P3D`` renderer. 

If you want a background to show up in your files, use ``rect(0, 0, width, height)`` after setting the ``fill()`` to the background color. Otherwise the background will not be rendered to the file because the background is not shape.

Using ``hint(ENABLE_DEPTH_SORT)`` can improve the appearance of 3D geometry drawn to 2D file formats.

See examples in the reference for the ``PDF`` and ``DXF`` libraries for more information.

Underlying Java method: `beginRaw <https://processing.org/reference/beginRaw_.html>`_

Syntax
======

.. code:: python

    begin_raw(raw_graphics: Py5Graphics) -> None
    begin_raw(renderer: str, filename: str) -> Py5Graphics

Parameters
==========

* **filename**: `str` - filename for output
* **raw_graphics**: `Py5Graphics` - ???
* **renderer**: `str` - for example, PDF or DXF


Updated on November 10, 2020 15:41:45pm UTC

