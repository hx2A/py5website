.. title: The Three py5 Modes
.. slug: py5-modes
.. date: 2021-01-07 13:47:11 UTC-05:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

The py5 is similar to `Processing <https://processing.org/>`_ and `p5 <https://p5js.org/>`_ in that the basic functionality comes from user implemented ``settings``, ``setup``, and ``draw`` methods. These methods will initialize the sketch parameters, run one-time setup code, and draw each frame of your animation.

In addition, py5 supports keyboard and mouse events with methods like ``mouseClicked`` and ``keyPressed``.

All of this is analogous to what users familiar with `Processing <https://processing.org/>`_ and `p5 <https://p5js.org/>`_ might expect.

The py5 library has three "modes" you can use to code these methods and write sketches. They are called Module Mode, Class Mode, and PDE Mode.

.. contents:: py5 Modes:
    :depth: 1
    :backlinks: top

.. important::

  There is a known problem using py5 on Mac computers. The best option for Mac users seems to be using py5 through :doc:`jupyter-notebooks`, and after using the ``%gui osx`` magic.

Module Mode
===========

Module Mode lets you write standalone ``settings``, ``setup``, and ``draw`` methods. Technically none are required but generally you will always use ``settings`` and one or both of ``setup`` and ``draw``.

In Module Mode, you will access py5 functionality through module-level functions and fields.

Below is a simple example:

.. code:: python

    import py5


    def settings():
        py5.size(300, 200)

    def setup():
        py5.rect_mode(py5.CENTER)
        
    def draw():
        py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

    py5.run_sketch()

This will create a small sketch that draws rectangles at the current mouse position.

Let's explain each part of the code.

The first statement imports the ``py5`` library in the same way that you would import any other Python library.

.. code:: python

    import py5

Next, the ``settings`` function. Here you will configure special sketch settings, such as the window size. In this example the window size is 300 pixels wide and 200 pixels tall. Almost always you'll have a ``settings`` function similar to this one. 

Notice the call to the :doc:`size` function has a "``py5.``" prefix. All of the py5 methods and fields are module level attributes.

.. code:: python

    def settings():
        py5.size(300, 200)

Next, the ``setup`` function. This function will be called one single time before beginning to repeatedly call the ``draw`` function for each frame of the animation. Typically the ``setup`` function is used to initialize variables or set py5 drawing options.

In this example, the call to :doc:`rect_mode` configures drawing options for future calls to py5's :doc:`rect` method. By default the first two coordinates specify the shape's upper left hand corner, but in this example they will specify the shape's center.

.. code:: python

    def setup():
        py5.rect_mode(py5.CENTER)

If the ``draw`` function is not found, the sketch will display a static image using draw commands found in the ``setup`` function. If the ``draw`` function is found, it will be repeatedly called once for each frame of an animation.

In this example, we draw one 10 by 10 pixel rectangle centered at the current mouse position. Accessing the module variables :doc:`mouse_x` and :doc:`mouse_y` will always provide the mouse's x and y coordinates.

.. code:: python

    def draw():
        py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

Finally, the call to :doc:`run_sketch`. This is will open a window and display your animation.

.. code:: python

    py5.run_sketch()

Note by default the call to :doc:`run_sketch` will not return until the sketch exits, unless if it is running from a Jupyter notebook or the IPython console. In that case it will return right away so the user can continue working in other cells in the notebook. Read the :doc:`run_sketch` documentation to learn more.

The design of Module Mode is modeled after matplotlib's pyplot.

.. caution::

    Do not use wildcard import syntax with the py5 library:

    .. code:: python

        from py5 import *

    Doing so would import usable methods, but the fields, such as ``mouse_x`` and ``mouse_y`` in the example above, would not work correctly. This is because py5's Module Mode is dependent on the module ``__getattr__`` and ``__dir__`` functionality described in `PEP 562 <https://www.python.org/dev/peps/pep-0562/>`_.

    Wildcard imports also conflict with `Python best practices (PEP 8) <https://www.python.org/dev/peps/pep-0008/#id23>`_ and in general should not be used.

    If you don't like prefixing everything with "``py5.``", use PDE Mode instead.

.. admonition:: Side Note

    Much like you would do for a Processing sketch, you may want to put supporting materials in a ``data`` subdirectory. A py5 sketch will look for this relative to the current working directory. You can find out what the current working directory is and change it with the ``os`` standard library.

    .. code:: python

        >>> import os
        >>> os.chdir('/dir/that/contains/your/data/subdir')
        >>> print(os.getcwd())
        /dir/that/contains/your/data/subdir

    If that doesn't meet your needs, you can also set it explicitly when you call :doc:`run_sketch`.

    .. code:: python

        py5.run_sketch(py5_options=['--sketch-path=/dir/that/contains/your/data/subdir'])

Class Mode
==========

Class mode lets you create a class with its own ``settings``, ``setup``, and ``draw`` methods. The example above coded in Class Mode is as follows:

.. code:: python

    from py5 import Sketch


    class TestSketch(Sketch):

        def settings(self):
            self.size(300, 200)

        def setup(self):
            self.rect_mode(self.CENTER)

        def draw(self):
            self.rect(self.mouse_x, self.mouse_y, 10, 10)


    test = TestSketch()
    test.run_sketch()

Let us again explain each part of the code.

The first line imports the ``Sketch`` class, which will provide the py5 functionality.

.. code:: python

    from py5 import Sketch

Next, define a new class that inherits from ``Sketch``.

.. code:: python

    class TestSketch(Sketch):

Each of the ``settings``, ``setup``, and ``draw`` methods have a ``self`` parameter, just as they would in any Python class. The ``self`` parameter is used to access the ``py5`` methods and fields provided by the parent ``Sketch`` class. Observe that every occurance of the "``py5.``" prefix in the Module Mode example has been replaced with "``self.``".

.. code:: python

        def settings(self):
            self.size(300, 200)

        def setup(self):
            self.rect_mode(self.CENTER)

        def draw(self):
            self.rect(self.mouse_x, self.mouse_y, 10, 10)

Finally, create an instance of the new class and call :doc:`run_sketch`.

.. code:: python

    test = TestSketch()
    test.run_sketch()

As before, the call to :doc:`run_sketch` will not return until the sketch exits, unless if it is running from a Jupyter notebook or the IPython console.

When developing in Jupyter notebooks, Module Mode is the more convenient choice.

Class mode will let you run multiple sketches at the same time. This cannot be done in Module Mode.

.. caution::

    When learning to use py5, you may accidentally conflate Module Mode and Class Mode by writing code like this:

    .. code:: python

            def draw(self):
                self.rect(py5.mouse_x, py5.mouse_y, 10, 10)

    Do you see the mistake?

    The ``py5.mouse_x`` and ``py5.mouse_y`` code is suitable for Module Mode, so it is referencing the mouse position in a special default sketch object found in the py5 module. However, in Class Mode you will create your own sketch object, and as is being done here, call your sketch object's ``rect`` method. This code is accidentally mixing one sketch's methods with another's fields. This is most certainly not what is intended, and any error message will not properly explain what is wrong.

    This mistake will frequently be made when translating py5 code from one mode to another.

    A good way to avoid this is to import the library with only one of "``import py5``" or "``from py5 import Sketch``", depending on which mode you want to use. Importing both ways is asking for trouble.

PDE Mode
========

PDE Mode is designed to used by beginner programmers in an environment like the Processing Development Editor (PDE). The Processing editor does not currently support py5, but perhaps one day it will.

Below is our example sketch written in PDE Mode:

.. code:: python

    def settings():
        size(300, 200)

    def setup():
        rect_mode(CENTER)
        
    def draw():
        rect(mouse_x, mouse_y, 10, 10)

Observe that any "``py5.``" and "``self.``" prefixes are removed. There is no "``import py5``" statement or call to :doc:`run_sketch`.

To actually use this, save your code to a file and execute the below command from a terminal:

.. code:: bash

    $ run_sketch test_sketch.py

The ``run_sketch`` command is installed for you when you install the py5 library. The running sketch will be identical to the other examples.

In PDE Mode, the ``settings`` function is no longer necessary if its contents are included in the ``setup`` function. This is analogous to what the PDE does for user code when using Processing in the PDE. When using Processing outside of the PDE, you must code a ``settings`` function, but inside the PDE, you put the ``settings`` code in ``setup``.

.. code:: python

    def setup():
        size(300, 200)
        rect_mode(CENTER)
        
    def draw():
        rect(mouse_x, mouse_y, 10, 10)

In PDE Mode you can also write code with no functions at all, similar to what can be done in with Processing in the Processing PDE:

.. code:: python

    size(300, 200)
    background(255)
    fill(255, 0, 0)
    rect_mode(CENTER)
    rect(150, 180, 10, 10)

This will create a non-animated sketch featuring a red square with white background.

PDE Mode will be more interesting and useful once it is integrated into a suitable editor such as the PDE, or maybe a different editor intended for Python like `Thonny <https://thonny.org/>`_ or `Mu <https://codewith.mu/>`_.

The operation of PDE Mode does some inefficient things behind the scenes in order to work correctly, and has a few bugs. This is fixable but will require some C coding.

.. important::

    When coding in PDE Mode without a ``settings`` function or with no functions at all, behind the scenes the py5 library is transforming your code into the standard ``settings``, ``setup``, and ``draw`` structure. As a consequence, the line numbers in the stack traces of any error messages will be a little bit off. This is disadvantageous to beginners and I intend to improve this at a later date.
