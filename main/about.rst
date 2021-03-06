.. title: About py5
.. slug: about
.. date: 2020-10-26 15:56:21 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. hidetitle: True


What is py5?
============

Py5 is a creative coding framework for Python 3.8+. Its use and functionality is analogous to the widely used Processing_ framework. It is a Python version of Processing_.

Internally py5 uses Processing_'s core libraries, which are written in Java, while providing the end user with a (mostly) seamless Python programming experience.

I started working on py5 in the Spring of 2020 when I was a Research Resident at ITP_. It began as a diversion from my pandemic-related anxieties and grew into the library it is today. I intend to use it as an outlet for my artistic endeavors involving Python's machine learning and data science tools and want to make it available and useful for other artists to do the same.

The py5 library itself is created by the meta-programming project py5generator. The `source code for py5 <https://github.com/hx2A/py5>`_ and `the source code for py5generator <https://github.com/hx2A/py5generator>`_ are both available on github.

Acknowledgments
===============

I'd like to thank and acknowledge all the people who helped make py5 possible.

- `Ben Fry <https://benfry.com/>`_, `Casey Reas <http://reas.com/>`_, and `the rest of the Processing team <https://github.com/processing/processing4/graphs/contributors?from=2019-10-01&to=2021-01-01&type=c>`_. Processing_ has been around for almost 20 years and is used by thousands for creative coding projects. Much of py5's functionality is provided by the Processing core libraries. Py5 stands on the shoulders of giants.

- `Jonathan Feinberg <http://mrfeinberg.com/>`_ and the rest of the `Processing.py <https://py.processing.org/>`_ contributors. Processing.py is a Jython version of Processing_, combining the same Processing core libraries that py5 utilizes with `Jython <https://www.jython.org/>`_, a Java implementation of Python. Processing.py is the spiritual ancestor to and inspiration for py5. Py5 is similar to Processing.py in that both use Python syntax but their implementations are very different. Processing.py and py5 do not share any code but py5 benefits from code in the Processing core libraries written to accommodate Processing.py.

  I'd also like to thank Jonathan Feinberg for building the awesome Processing library `PeasyCam <http://mrfeinberg.com/peasycam/>`_. PeasyCam is one of the Processing libraries I know to work well in py5.

- The developers of the JPype_ and `PyJNIus <https://github.com/kivy/pyjnius>`_ Python libraries. Both of these libraries allow Python code to interact with Java code in the Java Virtual Machine using `JNI <https://en.wikipedia.org/wiki/Java_Native_Interface>`_. Py5 originally used PyJNIus but later switched to JPype. PyJNIus is maintained by the `Kivy <https://kivy.org/>`_ project (which I am a member of). JPype's lead developer `Thrameos <https://github.com/Thrameos>`_ introduced us to their library and motivated me to switch.

- `Lauren McCarthy <https://lauren-mccarthy.com/>`_, who created `p5.js <https://p5js.org/>`_, a JavaScript version of Processing. Lauren helped me understand the importance of developing the :doc:`Community`. It is from p5 that py5 gets its name.

- The ITP_ faculty, including `Tom Igoe <https://tigoe.com/>`_, `Dan Shiffman <https://shiffman.net/>`_, and `Allison Parrish <https://www.decontextualize.com/>`_. All provided early feedback that provided guidance and helped keep me motivated. Allison also helped me understand the importance and value of the integrating py5 with Jupyter notebooks. 

- The ITP_ residents of 2019 to 2020, for putting up with me and being available to bounce ideas off of as I was in the early stages of developing this idea.

.. _Processing: https://processing.org/
.. _ITP: https://tisch.nyu.edu/itp
.. _JPype: https://github.com/jpype-project/jpype/
