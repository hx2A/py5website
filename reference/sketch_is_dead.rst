.. title: is_dead
.. slug: is_dead
.. date: 2021-03-07 16:32:04 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 is_dead documentation
.. type: text

Boolean value stating if the Sketch has been run and has now stopped.

Description
===========

Boolean value stating if the Sketch has been run and has now stopped. This will be ``True`` after calling :doc:`exit_sketch` or if the Sketch throws an error and stops. This will also be ``True`` after calling :doc:`py5surface`'s :doc:`py5surface_stop_thread` method. Once a Sketch reaches the "dead" state, it cannot be rerun.

After an error or a call to :doc:`py5surface_stop_thread`, the Sketch window will still be open. Call :doc:`exit_sketch` to close the window.


Updated on March 07, 2021 16:32:04pm UTC

