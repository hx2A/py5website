.. title: New Release: 0.3a5
.. slug: new-release-03a5
.. date: 2021-02-04 17:27:47 UTC-05:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

What's new:

* Upgrade to the Processing 4.0 alpha 3 release
* A new way of using py5: The :doc:`render-helper-tools`. This was a great idea suggested by `Allison Parrish <https://www.decontextualize.com/>`_.
* Major cleanup of the IPython Magics to make the magic names and their parameters more consistent. Notably, the units for all time related parameters is now in seconds. Any code that used the magics will need to be updated. Refer to the :doc:`jupyter-notebooks` documentation or the magic docstrings for more information.
* An exciting new feature to simplify the creation of adhoc Java extensions to boost Sketch performance. I haven't had a chance to document it yet, but trust me, it is pretty neat.

Also:

* Lots of little bug fixes
* Code improvements in the service of producing better documentation
* Changes to the setup.py package requirements

What's Ahead:

* Fixing OSX-specific issues
* Documentation, documentation, and documentation
