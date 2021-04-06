.. title: has_thread()
.. slug: has_thread
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 has_thread() documentation
.. type: text

Determine if a thread of a given name exists and is currently running.

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
        print('starting slow thread')
        time.sleep(7)
        print('finishing slow thread')


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

Determine if a thread of a given name exists and is currently running. You can get the list of all currently running threads with :doc:`list_threads`.

Syntax
======

.. code:: python

    has_thread(name: str) -> None

Parameters
==========

* **name**: `str` - name of thread


Updated on April 06, 2021 18:19:03pm UTC

