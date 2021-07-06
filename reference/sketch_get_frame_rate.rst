.. title: get_frame_rate()
.. slug: get_frame_rate
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 get_frame_rate() documentation
.. type: text

Get the running Sketch's current frame rate.

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

    def draw():
        py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
        py5.println(py5.get_frame_rate())

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Get the running Sketch's current frame rate. This is measured in frames per second (fps) and uses an exponential moving average. The returned value will not be accurate until after the Sketch has run for a few seconds. You can set the target frame rate with :doc:`frame_rate`.

This method provides the same information as Processing's ``frameRate`` variable. Python can't have a variable and a method with the same name, so a new method was created to provide access to that variable.

Underlying Java method: getFrameRate

Syntax
======

.. code:: python

    get_frame_rate() -> float

Updated on July 06, 2021 22:46:12pm UTC

