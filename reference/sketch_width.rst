.. title: width
.. slug: width
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 width documentation
.. type: text

System variable that stores the width of the display window.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_width_0.png
    :alt: example picture for width

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    no_stroke()
    background(0)
    rect(0, 40, width, 20)
    rect(0, 60, width//2, 20)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

System variable that stores the width of the display window. This value is set by the first parameter of the ``size()`` function. For example, the function call ``size(320, 240)`` sets the ``width`` variable to the value 320. The value of ``width`` defaults to 100 if ``size()`` is not used in a program.

Underlying Java field: `width <https://processing.org/reference/width.html>`_


Updated on November 10, 2020 15:41:45pm UTC

