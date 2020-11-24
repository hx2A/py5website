.. title: run_sketch()
.. slug: run_sketch
.. date: 2020-11-24 21:22:32 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 run_sketch() documentation
.. type: text

Run the sketch.

Description
===========

Run the sketch. Code in the ``settings``, ``setup``, and ``draw`` functions will be used to actualize your sketch.

Use the ``block`` parameter to specify if the call to ``run_sketch`` should return immediately or block until the sketch exits. If the ``block`` parameter is not specified, py5 will first attempt to determine if the sketch is running in a Jupyter Notebook or an IPython shell. If it is, ``block`` will default to ``False``, and ``True`` otherwise.

A list of strings passed to ``py5_options`` will be passed to the Processing PApplet class as arguments to specify characteristics such as the window's location on the screen. A list of strings passed to ``sketch_args`` will be available to a running sketch using :doc:`args`. For example, if you launch a sketch with ``py5.run_sketch(py5_options=['--location=400,300', '--display=1'], sketch_args=['py5 is awesome'])``, the sketch window will appear at location (400, 300) on your second monitor and ``py5.args`` will equal ``['py5 is awesome']``.

Syntax
======

.. code:: python

    run_sketch(block: bool = None, py5_options: List = None, sketch_args: List = None) -> None

Parameters
==========

* **block**: `bool = None` - method returns immediately (False) or blocks until sketch exits (True)
* **py5_options**: `List = None` - command line arguments to pass to Processing as arguments
* **sketch_args**: `List = None` - command line arguments that become Sketch arguments


Updated on November 24, 2020 21:22:32pm UTC

