.. title: launch_promise_thread()
.. slug: launch_promise_thread
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 launch_promise_thread() documentation
.. type: text

Create a ``Py5Promise`` object that will store the returned result of a function when that function completes.

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

    def setup():
        py5.size(250, 100)
        global promise
        promise = py5.launch_promise_thread(load_data)


    def load_data():
        return py5.load_json('http://py5.ixora.io/secret_message.json')


    def draw():
        py5.background(0)
        if promise.is_ready:
            py5.text(promise.result['msg'][:(py5.frame_count // 25)], 20, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Create a ``Py5Promise`` object that will store the returned result of a function when that function completes. This can be useful for executing non-py5 code that would otherwise slow down the animation thread and reduce the Sketch's frame rate.

The ``Py5Promise`` object has an ``is_ready`` property that will be ``True`` when the ``result`` property contains the value function ``f`` returned. Before then, the ``result`` property will be ``None``.

The ``name`` parameter is optional but useful if you want to monitor the thread with other methods such as :doc:`has_thread`. If the provided ``name`` is identical to an already running thread, the running thread will first be stopped with a call to :doc:`stop_thread` with the ``wait`` parameter equal to ``True``.

Use the ``args`` and ``kwargs`` parameters to pass positional and keyword arguments to the function.

Use the ``daemon`` parameter to make the launched thread a daemon that will run without blocking Python from exiting. This parameter defaults to ``True``, meaning that function execution can be interupted if the Python process exits. Note that if the Python process continues running after the Sketch exits, which is typically the case when using a Jupyter Notebook, this parameter won't have any effect unless if you try to restart the Notebook kernel. Generally speaking, setting this parameter to ``False`` causes problems but it is available for those who really need it. See :doc:`stop_all_threads` for a better approach to exit threads.

The new thread is a Python thread, so all the usual caveats about the Global Interpreter Lock (GIL) apply here.

Syntax
======

.. code:: python

    launch_promise_thread(f: Callable, name: str = None, *, daemon: bool = True, args: Tuple = None, kwargs: Dict = None) -> Py5Promise

Parameters
==========

* **args**: `Tuple = None` - positional arguments to pass to the given function
* **daemon**: `bool = True` - if the thread should be a daemon thread
* **f**: `Callable` - function to call in the launched thread
* **kwargs**: `Dict = None` - keyword arguments to pass to the given function
* **name**: `str = None` - name of thread to be created


Updated on June 28, 2021 15:16:14pm UTC

