.. title: begin_record()
.. slug: begin_record
.. date: 2021-02-16 16:54:21 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 begin_record() documentation
.. type: text

Opens a new file and all subsequent drawing functions are echoed to this file as well as the display window.

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

    def settings():
        py5.size(400, 400)


    def setup():
        py5.begin_record(py5.PDF, "everything.pdf")


    def draw():
        py5.ellipse(py5.mouse_x, py5.mouse_y, 10, 10)


    def mouse_pressed():
        py5.end_record()
        py5.exit_sketch()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Opens a new file and all subsequent drawing functions are echoed to this file as well as the display window. The ``begin_record()`` function requires two parameters, the first is the renderer and the second is the file name. This function is always used with ``end_record()`` to stop the recording process and close the file.

Note that ``begin_record()`` will only pick up any settings that happen after it has been called. For instance, if you call ``text_font()`` before ``begin_record()``, then that font will not be set for the file that you're recording to.

``begin_record()`` works only with the PDF and SVG renderers.

Underlying Java method: `beginRecord <https://processing.org/reference/beginRecord_.html>`_

Syntax
======

.. code:: python

    begin_record(recorder: Py5Graphics, /) -> None
    begin_record(renderer: str, filename: str, /) -> Py5Graphics

Parameters
==========

* **filename**: `str` - filename for output
* **recorder**: `Py5Graphics` - missing variable description
* **renderer**: `str` - PDF or SVG


Updated on February 16, 2021 16:54:21pm UTC

