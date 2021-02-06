.. title: %%py5drawsvg
.. slug: py5drawsvg
.. date: 2021-02-06 21:15:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 %%py5drawsvg documentation
.. type: text

Create a SVG drawing with py5 and embed result in the notebook.

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

    %%py5drawsvg 200 200
    py5.background(128)
    py5.fill(255, 0, 0)
    py5.rect(80, 100, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Create a SVG drawing with py5 and embed result in the notebook.

For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed in a sketch with no ``draw()`` function and your code in the ``setup()`` function. It will use the SVG renderer.

As this is creating a SVG drawing, you cannot do operations on the ``pixels`` or ``np_pixels`` arrays. Use ``%%py5draw`` instead.

Code used in this cell can reference functions and variables defined in other cells. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. If you understand the risks, you can use the ``global`` keyword to add a single function or variable to the notebook namespace or the ``--unsafe`` argument to add everything to the notebook namespace. Either option may be very useful to you, but be aware that using py5 objects in a different notebook cell or reusing them in another sketch can result in nasty errors and bizzare consequences.

Usage
=====

.. code::

    %%py5drawsvg [-f FILENAME] [--unsafe] width height

Arguments
=========

.. code::

    positional arguments:
      width                 width of SVG drawing
      height                height of SVG drawing

    optional arguments:
      -f FILENAME, --filename FILENAME
                            save SVG drawing to file
      --unsafe              allow new variables to enter the global namespace

Updated on February 06, 2021 21:15:00pm UTC

