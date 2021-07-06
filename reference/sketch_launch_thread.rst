.. title: launch_thread()
.. slug: launch_thread
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 launch_thread() documentation
.. type: text

Launch a new thread to execute a function in parallel with your Sketch code.

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

    import time


    def slow_thread():
        py5.println('starting slow thread')
        time.sleep(7)
        py5.println('finishing slow thread')


    def setup():
        py5.launch_thread(slow_thread, name='slow thread')


    def draw():
        if py5.has_thread('slow thread'):
            py5.background(0, 255, 0)
        else:
            py5.background(255, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Launch a new thread to execute a function in parallel with your Sketch code. This can be useful for executing non-py5 code that would otherwise slow down the animation thread and reduce the Sketch's frame rate.

The ``name`` parameter is optional but useful if you want to monitor the thread with other methods such as :doc:`has_thread`. If the provided ``name`` is identical to an already running thread, the running thread will first be stopped with a call to :doc:`stop_thread` with the ``wait`` parameter equal to ``True``.

Use the ``args`` and ``kwargs`` parameters to pass positional and keyword arguments to the function.

Use the ``daemon`` parameter to make the launched thread a daemon that will run without blocking Python from exiting. This parameter defaults to ``True``, meaning that function execution can be interupted if the Python process exits. Note that if the Python process continues running after the Sketch exits, which is typically the case when using a Jupyter Notebook, this parameter won't have any effect unless if you try to restart the Notebook kernel. Generally speaking, setting this parameter to ``False`` causes problems but it is available for those who really need it. See :doc:`stop_all_threads` for a better approach to exit threads.

The new thread is a Python thread, so all the usual caveats about the Global Interpreter Lock (GIL) apply here.

Syntax
======

.. code:: python

    launch_thread(f: Callable, name: str = None, *, daemon: bool = True, args: Tuple = None, kwargs: Dict = None) -> str

Parameters
==========

* **args**: `Tuple = None` - positional arguments to pass to the given function
* **daemon**: `bool = True` - if the thread should be a daemon thread
* **f**: `Callable` - function to call in the launched thread
* **kwargs**: `Dict = None` - keyword arguments to pass to the given function
* **name**: `str = None` - name of thread to be created


Updated on July 06, 2021 22:46:12pm UTC

