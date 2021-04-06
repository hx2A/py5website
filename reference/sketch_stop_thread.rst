.. title: stop_thread()
.. slug: stop_thread
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 stop_thread() documentation
.. type: text

Stop a thread of a given name.

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

    def pick_color():
        global color
        color = py5.random_int(255), py5.random_int(255), py5.random_int(255)


    def setup():
        py5.launch_repeating_thread(pick_color, name='pick_color', time_delay=1)


    def draw():
        py5.background(*color)
        if py5.frame_count == 500:
            py5.stop_thread('pick_color')

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Stop a thread of a given name. The ``wait`` parameter determines if the method call will return right away or wait for the thread to exit.

This won't do anything useful if the thread was launched with either :doc:`launch_thread` or :doc:`launch_promise_thread` and the ``wait`` parameter is ``False``. Non-repeating threads are executed once and will stop when they complete execution. Setting the ``wait`` parameter to ``True`` will merely block until the thread exits on its own. Killing off a running thread in Python is complicated and py5 cannot do that for you. If you want a thread to perform some action repeatedly and be interuptable, use :doc:`launch_repeating_thread` instead.

Use :doc:`has_thread` to determine if a thread of a given name exists and :doc:`list_threads` to get a list of all thread names. Use :doc:`stop_all_threads` to stop all threads.

Syntax
======

.. code:: python

    stop_thread(name: str, wait: bool = False) -> None

Parameters
==========

* **name**: `str` - name of thread
* **wait**: `bool = False` - wait for thread to exit before returning


Updated on April 06, 2021 18:19:03pm UTC

