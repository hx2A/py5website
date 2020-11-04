.. title: create_shape()
.. slug: sketch_create_shape
.. date: 2020-11-04 20:45:44 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 create_shape() documentation
.. type: text

The ``create_shape()`` function is used to define a new shape.

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

    def setup():
        global square  # the Py5Shape object
        size(100, 100)
        # creating the Py5Shape as a square. the
        # numeric arguments are similar to rect().
        square = create_shape(RECT, 0, 0, 50, 50)
        square.set_fill(color(0, 0, 255))
        square.set_stroke(False)


    def draw():
        shape(square, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s  # the Py5Shape object
        size(100, 100)
        # creating a custom Py5Shape as a square, by
        # specifying a series of vertices.
        s = create_shape()
        s.begin_shape()
        s.fill(0, 0, 255)
        s.no_stroke()
        s.vertex(0, 0)
        s.vertex(0, 50)
        s.vertex(50, 50)
        s.vertex(50, 0)
        s.end_shape(CLOSE)


    def draw():
        shape(s, 25, 25)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        global s
        size(100, 100, P2D)
        s = create_shape()
        s.begin_shape(TRIANGLE_STRIP)
        s.vertex(30, 75)
        s.vertex(40, 20)
        s.vertex(50, 75)
        s.vertex(60, 20)
        s.vertex(70, 75)
        s.vertex(80, 20)
        s.vertex(90, 75)
        s.end_shape()


    def draw():
        shape(s, 0, 0)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    Py5Shape alien, head, body


    def setup():
        size(100, 100)

        # create the shape group
        alien = create_shape(GROUP)

        # make two shapes
        ellipse_mode(CORNER)
        head = create_shape(ELLIPSE, -25, 0, 50, 50)
        head.set_fill(color(255))
        body = create_shape(RECT, -25, 45, 50, 40)
        body.set_fill(color(0))

        # add the two "child" shapes to the parent group
        alien.add_child(body)
        alien.add_child(head)


    def draw():
        background(204)
        translate(50, 15)
        shape(alien)  # draw the group

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

The ``create_shape()`` function is used to define a new shape. Once created, this shape can be drawn with the ``shape()`` function. The basic way to use the function defines new primitive shapes. One of the following parameters are used as the first parameter: ``ELLIPSE``, ``RECT``, ``ARC``, ``TRIANGLE``, ``SPHERE``, ``BOX``, ``QUAD``, or ``LINE``. The parameters for each of these different shapes are the same as their corresponding functions: ``ellipse()``, ``rect()``, ``arc()``, ``triangle()``, ``sphere()``, ``box()``, ``quad()``, and ``line()``. The first example above clarifies how this works.

Custom, unique shapes can be made by using ``create_shape()`` without a parameter. After the shape is started, the drawing attributes and geometry can be set directly to the shape within the ``begin_shape()`` and ``end_shape()`` methods. See the second example above for specifics, and the reference for ``begin_shape()`` for all of its options.

The  ``create_shape()`` function can also be used to make a complex shape made of other shapes. This is called a "group" and it's created by using the parameter ``GROUP`` as the first parameter. See the fourth example above to see how it works.

After using ``create_shape()``, stroke and fill color can be set by calling methods like ``set_fill()`` and ``set_stroke()``, as seen in the examples above. The complete list of methods and fields for the PShape class are in the Processing Javadoc.

Underlying Java method: `createShape <https://processing.org/reference/createShape_.html>`_

Syntax
======

.. code:: python

    create_shape() -> Py5Shape
    create_shape(kind: int, p: float) -> Py5Shape
    create_shape(type: int) -> Py5Shape

Parameters
==========

* **kind**: `int` - either POINT, LINE, TRIANGLE, QUAD, RECT, ELLIPSE, ARC, BOX, SPHERE
* **p**: `float` - parameters that match the kind of shape
* **type**: `int` - missing variable description


Updated on November 04, 2020 20:45:44pm UTC

