.. title: %py5screenshot
.. slug: py5screenshot
.. date: 2021-02-06 21:15:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 %py5screenshot documentation
.. type: text

Take a screenshot of the current running sketch.

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

    py5.run_sketch()
    # take a screenshot of the running sketch after a two second delay
    img = %py5screenshot -w 2
    img.save('image.png')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Take a screenshot of the current running sketch.

Use the ``-w`` argument to wait before taking the screenshot.

The returned image is a ``PIL.Image`` object. It can be assigned to a variable or embedded in the notebook.

Usage
=====

.. code::

    %py5screenshot [-w WAIT]

Arguments
=========

.. code::

    optional arguments:
      -w WAIT, --wait WAIT  wait time in seconds before taking screenshot

Updated on February 06, 2021 21:15:00pm UTC

