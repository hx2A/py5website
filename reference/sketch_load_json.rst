.. title: load_json()
.. slug: load_json
.. date: 2021-04-06 18:19:03 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 load_json() documentation
.. type: text

Load a JSON data file from a file or URL.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_load_json_0.png
    :alt: example picture for load_json()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def setup():
        data = py5.load_json('colors.json')
        py5.fill(data['red'], data['green'], data['blue'])
        py5.rect(10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    def settings():
        py5.size(250, 100)


    def load_data():
        return py5.load_json('http://py5.ixora.io/secret_message.json')


    def setup():
        global promise
        promise = py5.launch_promise_thread(load_data)


    def draw():
        py5.background(0)
        if promise.is_ready:
            py5.text(promise.result['msg'][:(py5.frame_count // 25)], 20, 50)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Load a JSON data file from a file or URL. When loading a file, the path can be in the data directory, relative to the current working directory (:doc:`sketch_path`), or an absolute path. When loading from a URL, the ``json_path`` parameter must start with ``http://`` or ``https://``.

When loading JSON data from a URL, the data is retrieved using the Python requests library with the ``get`` method, and the ``kwargs`` parameter is passed along to that method. When loading JSON data from a file, the data is loaded using the Python json library with the ``load`` method, and again the ``kwargs`` parameter passed along to that method.

Syntax
======

.. code:: python

    load_json(json_path: Union[str, Path], kwargs: Dict[str, Any]) -> Any

Parameters
==========

* **json_path**: `Union[str, Path]` - url or file path for JSON data file
* **kwargs**: `Dict[str, Any]` - keyword arguments


Updated on April 06, 2021 18:19:03pm UTC

