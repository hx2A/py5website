.. title: Special Notes for Mac Users
.. slug: mac-users
.. date: 2021-03-22 08:22:23 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

There are some difficulties using py5 on Mac computers that still need to be worked out.

.. admonition:: TL;DR

    * Mac users must use Jupyter Notebooks with the ``%gui osx`` magic at the start of each notebook.
    * New Sketch windows might not get focus and will be behind other windows.
    * Ignore the warnings you see when exiting a Sketch

JPype
=====

The py5 library uses the Python library JPype_ to create the Java-Python bridge between the two languages. There is currently `a bug in JPype that prevents Java GUI applications from running correctly on Mac computers <https://github.com/jpype-project/jpype/issues/906>`_. JPype's core developer does not have a Mac computer to test and fix the problem, and can't get access to one because of pandemic related issues. This is a problem, but let's keep things in perspective: the pandemic has taken a toll on all of us, with many people losing their lives or jobs. Software bugs and delays aren't a real problem. I'd like you to be patient with me while this gets worked out.

Jupyter Notebooks
=================

If you like Jupyter Notebooks, you're in luck! Everything will work just fine after executing the following IPython magic at the `start` of each notebook:

.. raw:: html

    <div class="cell border-box-sizing code_cell rendered">
    <div class="input">
    <div class="prompt input_prompt">In&nbsp;[1]:</div>
    <div class="inner_cell"><div class="input_area">
    <div class=" highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">gui</span> osx</pre></div>
    </div></div></div></div>

This must be executed `before` importing py5.

OSX has some requirement that only allows GUI applications to run on the main thread. That magic command configures things so that py5 can work. I don't understand how or why it works. I know that it works, and I am grateful.

If you forget to use the ``%osx gui`` magic, the Sketch will still run but will be invisible. You'll see the output of any ``print`` statements and the :doc:`frame_count` value will keep increasing. Any efforts to make the window appear using the Sketch's ``Py5Surface`` object will be in vain.

The ``%osx gui`` magic must be executed before the ``import py5`` statement. Running a script with the ``%run`` magic doesn't seem to work. The py5 Jupyter Notebook Kernel will take care of the ``%osx gui`` magic for you when run on a Mac computer.

If you like coding in an interactive terminal (I hope I'm not the only one), you will need to use ``jupyter console`` and not ``ipython``. The two interactive terminal applications are not identical, with the ``%gui osx`` magic working in the former but not the latter.

Mac users won't be able to use the generic ``python`` interpreter to run py5, either interactively or to run a python program. If you need to run a py5 application in a script, your best bet is to put your code in a notebook and execute the notebook, like so:

.. code:: bash

    $ jupyter nbconvert --execute --to notebook --inplace py5_code.ipynb

Of course you can always use a virtual machine or Docker, but those are more complicated to get working. Still, these are valid choices that might meet your needs.

I'm not an expert Mac user so it is very likely there is more to be said about using py5 on Macs. Please experiment based on your own knowledge and ideas. If you discover something useful, let me know and I'll update the documentation.

Window Focus & Dock Icons
=========================

The next problem has to do with the Dock Icons at the bottom of the screen.

If you run a Sketch that uses the default renderer, no icon will appear in the dock and the window may not be given focus. When you get tired of minimizing other windows to find the Sketch window, try using the Sketch's ``Py5Surface`` object to move it or bring it to the front, like so:

.. code:: python

    py5.run_sketch()
    surface = py5.get_surface()
    # move the Sketch window to a more convenient location
    surface.set_location(10, 10)
    # move the Sketch window to the top
    surface.set_always_on_top(True)

In the future I may be able to add code to compensate for the window focus issues. For now, the above workaround will suffice.

If you run a Sketch that uses the ``P2D`` or ``P3D`` renderers, a dock icon will appear, but when the Sketch exits, the dock icon will remain. The Sketch really has stopped running and the window really has been destroyed (if you can prove me wrong please tell me), but the dock icon will not disappear until after the JVM shuts down, which will typically be when the Python process stops (when the Jupyter Notebook Kernel stops). I'm not totally sure why this is; there might be some special Processing code that creates the dock icon without matching Processing code to remove it on Sketch exit. In any case, this is a cosmetic issue and shouldn't be a cause for concern.

Sketch Exit
===========

When the Sketch exits you will see the following warning:

.. code::

    NewtNSView::dealloc: softLock still hold @ dealloc!

Ignore that.

.. _JPype: https://jpype.readthedocs.io/en/latest/
