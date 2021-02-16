.. title: is_key_pressed
.. slug: is_key_pressed
.. date: 2021-02-14 14:51:53 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 is_key_pressed documentation
.. type: text

The ``is_key_pressed`` variable stores whether or not a keyboard button is currently being pressed.

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
        if py5.is_key_pressed:
            if py5.key in ['b', 'B']:
               py5.fill(0)
        else:
            py5.fill(255)

        py5.rect(25, 25, 50, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``is_key_pressed`` variable stores whether or not a keyboard button is currently being pressed. The value is true when `any` keyboard button is pressed, and false if no button is pressed. The :doc:`key` variable and :doc:`key_code` variables (see the related reference entries) can be used to determine which button has been pressed.


Updated on February 14, 2021 14:51:53pm UTC

