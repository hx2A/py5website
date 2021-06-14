.. title: New Release: 0.4a2
.. slug: new-release-04a2
.. date: 2021-06-13 21:08:15 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

What's new:

* py5 on `mybinder <https://mybinder.org/v2/gh/hx2A/py5examples/HEAD?urlpath=lab>`_
* Py5SketchPortal widget to view animations on mybinder
* New ``println`` method for correctly printing to stdout and stderr from Sketch methods when using Jupyter lab

Breaking changes:

* The IPython line magics such as ``%screenshot`` and ``%animatedgif`` are now ordinary functions in ``py5_tools``. They never should have been line magics in the first place.

Also:

* Some improvements for OSX Users. The OSX issues are now reduced from critical problems to annoyances
* Lots of little bug fixes

What's Ahead:

* Coding trick to allow users to skip a ``settings()`` method, like what can be done in the Processing IDE
* Write Tutorials and How-tos
* Expand example code in the py5examples repo
