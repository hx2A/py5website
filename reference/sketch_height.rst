.. title: height
.. slug: height
.. date: 2021-03-03 21:11:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 height documentation
.. type: text

System variable that stores the height of the display window.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_height_0.png
    :alt: example picture for height

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        py5.no_stroke()
        py5.background(0)
        py5.rect(40, 0, 20, py5.height)
        py5.rect(60, 0, 20, py5.height//2)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

System variable that stores the height of the display window. This value is set by the second parameter of the :doc:`size` function. For example, the function call ``size(320, 240)`` sets the ``height`` variable to the value 240. The value of ``height`` defaults to 100 if :doc:`size` is not used in a program.

Underlying Java field: `height <https://processing.org/reference/height.html>`_


Updated on March 03, 2021 21:11:14pm UTC

