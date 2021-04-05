.. title: parse_json()
.. slug: parse_json
.. date: 2021-04-05 00:15:34 UTC+00:00
.. tags:
.. category:
.. link:
.. description: py5 parse_json() documentation
.. type: text

Parse serialized JSON data from a string.

Examples
========

.. raw:: html

    <div class="example-table">

.. raw:: html

    <div class="example-row"><div class="example-cell-image">

.. image:: /images/reference/Sketch_parse_json_0.png
    :alt: example picture for parse_json()

.. raw:: html

    </div><div class="example-cell-code">

.. code:: python
    :number-lines:

    serialized_json = '{"red":255, "green":255, "blue":128}'

    def setup():
        data = py5.parse_json(serialized_json)
        py5.fill(data['red'], data['green'], data['blue'])
        py5.rect(10, 10, 80, 80)

.. raw:: html

    </div></div>

.. raw:: html

    </div>

Description
===========

Parse serialized JSON data from a string. When reading JSON data from a file, :doc:`load_json` is the better choice.

The JSON data is parsed using the Python json library with the ``loads`` method, and the ``kwargs`` parameter is passed along to that method.

Syntax
======

.. code:: python

    parse_json(serialized_json: Any, kwargs: Dict[str, Any]) -> Any

Parameters
==========

* **kwargs**: `Dict[str, Any]` - keyword arguments
* **serialized_json**: `Any` - JSON data object that has been serialized as a string


Updated on April 05, 2021 00:15:34am UTC

