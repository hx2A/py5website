.. title: Py5Shader.set()
.. slug: py5shader_set
.. date: 2021-06-28 15:16:14 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 Py5Shader.set() documentation
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
        py5.size(640, 360, py5.P2D)
        global tex
        global deform
        tex = py5.load_image("tex1.jpg")
        deform = py5.load_shader("deform.glsl")
        deform.set("resolution", float(py5.width), float(py5.height))


    def draw():
        deform.set("time", py5.millis() / 1000.0)
        deform.set("mouse", float(py5.mouse_x), float(py5.mouse_y))
        py5.shader(deform)
        py5.image(tex, 0, 0, py5.width, py5.height)

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

    set(name: str, boolvec: JArray(JBoolean), ncoords: int, /) -> None
    set(name: str, mat: NDArray[(2, 3), Float], /) -> None
    set(name: str, mat: NDArray[(4, 4), Float], /) -> None
    set(name: str, mat: NDArray[(4, 4), Float], use3x3: bool, /) -> None
    set(name: str, tex: Py5Image, /) -> None
    set(name: str, vec: JArray(JBoolean), /) -> None
    set(name: str, vec: NDArray[(Any,), Float], /) -> None
    set(name: str, vec: NDArray[(Any,), Float], ncoords: int, /) -> None
    set(name: str, vec: NDArray[(Any,), Int], /) -> None
    set(name: str, vec: NDArray[(Any,), Int], ncoords: int, /) -> None
    set(name: str, x: bool, /) -> None
    set(name: str, x: bool, y: bool, /) -> None
    set(name: str, x: bool, y: bool, z: bool, /) -> None
    set(name: str, x: bool, y: bool, z: bool, w: bool, /) -> None
    set(name: str, x: float, /) -> None
    set(name: str, x: float, y: float, /) -> None
    set(name: str, x: float, y: float, z: float, /) -> None
    set(name: str, x: float, y: float, z: float, w: float, /) -> None
    set(name: str, x: int, /) -> None
    set(name: str, x: int, y: int, /) -> None
    set(name: str, x: int, y: int, z: int, /) -> None
    set(name: str, x: int, y: int, z: int, w: int, /) -> None

Parameters
==========

* **boolvec**: `JArray(JBoolean)` - modifies all the components of an array/vector uniform variable
* **mat**: `NDArray[(2, 3), Float]` - numpy array of values
* **mat**: `NDArray[(4, 4), Float]` - numpy array of values
* **name**: `str` - the name of the uniform variable to modify
* **ncoords**: `int` - number of coordinates per element, max 4
* **tex**: `Py5Image` - sets the sampler uniform variable to read from this image texture
* **use3x3**: `bool` - enforces the numpy array is 3 x 3
* **vec**: `JArray(JBoolean)` - modifies all the components of an array/vector uniform variable
* **vec**: `NDArray[(Any,), Float]` - numpy array of values to modify all the components of an array/vector uniform variable
* **vec**: `NDArray[(Any,), Int]` - modifies all the components of an array/vector uniform variable
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


Updated on June 28, 2021 15:16:14pm UTC

