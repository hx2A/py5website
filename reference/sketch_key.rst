.. title: key
.. slug: key
.. date: 2020-11-10 15:41:45 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 key documentation
.. type: text

The system variable ``key`` always contains the value of the most recent key on the keyboard that was used (either pressed or released).

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

    # click on the window to give it focus,
    # and press the 'b' key.

    def draw():
        if key_pressed:
            if key == 'b' | | key == 'b':
                fill(0)

        else:
            fill(255)

        rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The system variable ``key`` always contains the value of the most recent key on the keyboard that was used (either pressed or released). 
 
For non-ASCII keys, use the ``key_code`` variable. The keys included in the ASCII specification (BACKSPACE, TAB, ENTER, RETURN, ESC, and DELETE) do not require checking to see if the key is coded, and you should simply use the ``key`` variable instead of ``key_code`` If you're making cross-platform projects, note that the ENTER key is commonly used on PCs and Unix and the RETURN key is used instead on Macintosh. Check for both ENTER and RETURN to make sure your program will work for all platforms.

There are issues with how ``key_code`` behaves across different renderers and operating systems. Watch out for unexpected behavior as you switch renderers and operating systems.

Underlying Java field: `key <https://processing.org/reference/key.html>`_


Updated on November 10, 2020 15:41:45pm UTC
