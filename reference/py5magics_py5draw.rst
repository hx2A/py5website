.. title: %%py5draw
.. slug: py5draw
.. date: 2021-03-04 19:43:58 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 %%py5draw documentation
.. type: text

Create a PNG image with py5 and embed result in the notebook.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Py5Magics_py5draw_0.png
    :alt: example picture for %%py5draw

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    %%py5draw 200 200
    py5.background(128)
    py5.fill(255, 0, 0)
    py5.rect(80, 100, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Create a PNG image with py5 and embed result in the notebook.

For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed in a sketch with no ``draw()`` function and your code in the ``setup()`` function. By default it will use the default Processing renderer.

Code used in this cell can reference functions and variables defined in other cells. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. If you understand the risks, you can use the ``global`` keyword to add a single function or variable to the notebook namespace or the ``--unsafe`` argument to add everything to the notebook namespace. Either option may be very useful to you, but be aware that using py5 objects in a different notebook cell or reusing them in another sketch can result in nasty errors and bizzare consequences.

Usage
=====

.. code::

    %%py5draw [-f FILENAME] [-v VARIABLE] [-r RENDERER] [--unsafe] width height

Arguments
=========

.. code::

    positional arguments:
      width                 width of PNG image
      height                height of PNG image

    optional arguments:
      -f FILENAME, --filename FILENAME
                            save image to file
      -v VARIABLE, --var VARIABLE
                            assign image to variable
      -r RENDERER, --renderer RENDERER
                            processing renderer to use for sketch
      --unsafe              allow new variables to enter the global namespace

Updated on March 04, 2021 19:43:58pm UTC

