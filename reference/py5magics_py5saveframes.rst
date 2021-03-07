.. title: %py5saveframes
.. slug: py5saveframes
.. date: 2021-03-06 19:17:57 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 %py5saveframes documentation
.. type: text

Save the current running Sketch's frames to a directory.

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

    py5.run_sketch()
    # save the next 50 frames to the `/tmp/frames` directory
    %py5saveframes /tmp/frames -w 3 -s 0 --limit 50

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Save the current running Sketch's frames to a directory.

Use the ``-w`` argument to wait before starting.

If a limit is given, this line magic will wait to return a list of the filenames. Otherwise, it will return right away as the frames are saved in the background. It will keep doing so as long as the Sketch continues to run.

Usage
=====

.. code::

    %py5saveframes [-f FILENAME] [-w WAIT] [-p PERIOD] [-s START] [-l LIMIT] dirname

Arguments
=========

.. code::

    positional arguments:
      dirname               directory to save the frames

    optional arguments:
      -f FILENAME, --filename FILENAME
                            filename to save frames to
      -w WAIT, --wait WAIT  wait time in seconds before starting to save frames
      -p PERIOD, --period PERIOD
                            time in seconds between Sketch snapshots (default 0 means no delay)
      -s START, --start START
                            frame starting number instead of Sketch frame_count
      -l LIMIT, --limit LIMIT
                            limit the number of frames to save (default 0 means no limit)

Updated on March 06, 2021 19:17:57pm UTC

