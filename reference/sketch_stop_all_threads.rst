.. title: stop_all_threads()
.. slug: stop_all_threads
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 stop_all_threads() documentation
.. type: text

Stop all running threads.

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

    def thread1():
        py5.println('thread 1')


    def thread2():
        py5.println('thread 2')


    def setup():
        py5.frame_rate(10)
        py5.launch_repeating_thread(thread1, name='thread 1', time_delay=1.2)
        py5.launch_repeating_thread(thread2, name='thread 2', time_delay=1.8)


    def draw():
        py5.println('running threads:', ', '.join(py5.list_threads()))
        if py5.frame_count == 50:
            py5.stop_all_threads()

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Stop all running threads. The ``wait`` parameter determines if the method call will return right away or wait for the threads to exit.

When the Sketch shuts down, ``stop_all_threads(wait=False)`` is called for you. If you would rather the Sketch waited for threads to exit, create an ``exiting`` method and make a call to ``stop_all_threads(wait=True)``.

Syntax
======

.. code:: python

    stop_all_threads(wait: bool = False) -> None

Parameters
==========

* **wait**: `bool = False` - wait for thread to exit before returning


Updated on July 06, 2021 22:46:12pm UTC

