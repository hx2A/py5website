.. title: is_dead
.. slug: is_dead
.. date: 2021-07-06 22:46:12 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 is_dead documentation
.. type: text

Boolean value reflecting if the Sketch has been run and has now stopped.

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

    def setup():
        py5.background(255, 0, 0)


    py5.println("the sketch is ready:", py5.is_ready)

    py5.run_sketch()

    py5.println("the sketch is running:", py5.is_running)

    py5.exit_sketch()

    # wait for exit_sketch to complete
    time.sleep(1)

    py5.println("the sketch is dead:", py5.is_dead)
    py5.println("did the sketch exit from an error?", py5.is_dead_from_error)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Boolean value reflecting if the Sketch has been run and has now stopped. This will be ``True`` after calling :doc:`exit_sketch` or if the Sketch throws an error and stops. This will also be ``True`` after calling :doc:`py5surface`'s :doc:`py5surface_stop_thread` method. Once a Sketch reaches the "dead" state, it cannot be rerun.

After an error or a call to :doc:`py5surface_stop_thread`, the Sketch window will still be open. Call :doc:`exit_sketch` to close the window.


Updated on July 06, 2021 22:46:12pm UTC

