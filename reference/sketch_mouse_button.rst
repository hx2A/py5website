.. title: mouse_button
.. slug: mouse_button
.. date: 2021-02-13 18:02:35 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 mouse_button documentation
.. type: text

When a mouse button is pressed, the value of the system variable ``mouse_button`` is set to either ``LEFT``, ``RIGHT``, or ``CENTER``, depending on which button is pressed.

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

    # click within the image and press
    # the left and right mouse buttons to
    # change the value of the rectangle
    def draw():
        if py5.is_mouse_pressed() and py5.mouse_button == py5.LEFT:
            py5.fill(0)
        elif py5.is_mouse_pressed() and py5.mouse_button == py5.RIGHT:
            py5.fill(255)
        else:
            py5.fill(126)

        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    # click within the image and press
    # the left and right mouse buttons to
    # change the value of the rectangle
    def draw():
        py5.rect(25, 25, 50, 50)


    def mouse_pressed():
        if py5.mouse_button == py5.LEFT:
            py5.fill(0)
        elif py5.mouse_button == py5.RIGHT:
            py5.fill(255)
        else:
            py5.fill(126)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

When a mouse button is pressed, the value of the system variable ``mouse_button`` is set to either ``LEFT``, ``RIGHT``, or ``CENTER``, depending on which button is pressed. (If no button is pressed, ``mouse_button`` may be reset to ``0``. For that reason, it's best to use ``mouse_pressed`` first to test if any button is being pressed, and only then test the value of ``mouse_button``, as shown in the examples above.)

Underlying Java field: `mouseButton <https://processing.org/reference/mouseButton.html>`_


Updated on February 13, 2021 18:02:35pm UTC

