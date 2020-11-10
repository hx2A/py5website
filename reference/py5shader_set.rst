.. title: set()
.. slug: py5shader_set
.. date: 1970-01-01 00:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 set() documentation
.. type: text

Sets the uniform variables inside the shader to modify the effect while the program is running.

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
        global tex
        global deform
        size(640, 360, P2D)
        tex = load_image("tex1.jpg")
        deform = load_shader("deform.glsl")
        deform.set("resolution", float(width), float(height))


    def draw():
        deform.set("time", millis() / 1000.0)
        deform.set("mouse", float(mouse_x), float(mouse_y))
        shader(deform)
        image(tex, 0, 0, width, height)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Sets the uniform variables inside the shader to modify the effect while the program is running.

Underlying Java method: `PShader.set <https://processing.org/reference/PShader_set_.html>`_

Syntax
======

.. code:: python

    set(name: str, boolvec: JArray(JBoolean), ncoords: int) -> None
    set(name: str, mat: NDArray[(2, 3), Float]) -> None
    set(name: str, mat: NDArray[(4, 4), Float]) -> None
    set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool) -> None
    set(name: str, tex: Py5Image) -> None
    set(name: str, vec: JArray(JBoolean)) -> None
    set(name: str, vec: JArray(JInt)) -> None
    set(name: str, vec: JArray(JInt), ncoords: int) -> None
    set(name: str, vec: NDArray[(Any,), Float]) -> None
    set(name: str, vec: NDArray[(Any,), Float], ncoords: int) -> None
    set(name: str, x: bool) -> None
    set(name: str, x: bool, y: bool) -> None
    set(name: str, x: bool, y: bool, z: bool) -> None
    set(name: str, x: bool, y: bool, z: bool, w: bool) -> None
    set(name: str, x: float) -> None
    set(name: str, x: float, y: float) -> None
    set(name: str, x: float, y: float, z: float) -> None
    set(name: str, x: float, y: float, z: float, w: float) -> None
    set(name: str, x: int) -> None
    set(name: str, x: int, y: int) -> None
    set(name: str, x: int, y: int, z: int) -> None
    set(name: str, x: int, y: int, z: int, w: int) -> None

Parameters
==========

* **boolvec**: `JArray(JBoolean)` - missing variable description
* **mat**: `NDArray[(2, 3), Float]` - matrix of values
* **mat**: `NDArray[(4, 4), Float]` - matrix of values
* **name**: `str` - the name of the uniform variable to modify
* **ncoords**: `int` - number of coordinates per element, max 4
* **tex**: `Py5Image` - sets the sampler uniform variable to read from this image texture
* **use3x3**: `bool` - enforces the matrix is 3 x 3
* **vec**: `JArray(JBoolean)` - modifies all the components of an array/vector uniform variable. PVector can only be used if the type of the variable is vec3.
* **vec**: `JArray(JInt)` - modifies all the components of an array/vector uniform variable. PVector can only be used if the type of the variable is vec3.
* **vec**: `NDArray[(Any,), Float]` - modifies all the components of an array/vector uniform variable. PVector can only be used if the type of the variable is vec3.
* **w**: `bool` - fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)
* **w**: `float` - fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)
* **w**: `int` - fourth component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[4], vec4)
* **x**: `bool` - first component of the variable to modify
* **x**: `float` - first component of the variable to modify
* **x**: `int` - first component of the variable to modify
* **y**: `bool` - second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
* **y**: `float` - second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
* **y**: `int` - second component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[2], vec2)
* **z**: `bool` - third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
* **z**: `float` - third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)
* **z**: `int` - third component of the variable to modify. The variable has to be declared with an array/vector type in the shader (i.e.: int[3], vec3)


Updated on January 01, 1970 00:00:00am UTC

