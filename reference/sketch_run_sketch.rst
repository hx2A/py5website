.. title: run_sketch()
.. slug: run_sketch
.. date: 2021-03-06 19:17:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 run_sketch() documentation
.. type: text

Run the Sketch.

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

    py5.run_sketch(block=True)
    print("this message will not be printed until after the sketch exits")

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    py5.run_sketch(block=False)
    print("this message will be printed immediately, while the sketch is running")

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # run the sketch with the window at position 400, 300 on display #1
    py5.run_sketch(block=False, py5_options=['--location=400,300', '--display=1'], sketch_args=['py5 is awesome'])
    # this will print 'py5 is awesome'
    print(py5.args[0])

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Run the Sketch. Code in the ``settings``, ``setup``, and ``draw`` functions will be used to actualize your Sketch.

Use the ``block`` parameter to specify if the call to ``run_sketch`` should return immediately or block until the Sketch exits. If the ``block`` parameter is not specified, py5 will first attempt to determine if the Sketch is running in a Jupyter Notebook or an IPython shell. If it is, ``block`` will default to ``False``, and ``True`` otherwise.

A list of strings passed to ``py5_options`` will be passed to the Processing PApplet class as arguments to specify characteristics such as the window's location on the screen. A list of strings passed to ``sketch_args`` will be available to a running Sketch using :doc:`args`. See the third example for an example of how this can be used.

Syntax
======

.. code:: python

    run_sketch(block: bool = None, py5_options: List = None, sketch_args: List = None) -> None

Parameters
==========

* **block**: `bool = None` - method returns immediately (False) or blocks until Sketch exits (True)
* **py5_options**: `List = None` - command line arguments to pass to Processing as arguments
* **sketch_args**: `List = None` - command line arguments that become Sketch arguments


Updated on March 06, 2021 19:17:57pm UTC

