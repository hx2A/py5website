.. title: Acknowledgments
.. slug: acknowledgments
.. date: 2020-10-26 15:56:21 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

I'd like to thank and acknowledge all the people who helped make py5 possible.

- `Ben Fry <https://benfry.com/>`_, `Casey Reas <http://reas.com/>`_, and the rest of the Processing team. Processing_ has been around for almost 20 years and is used by thousands for creative coding projects. Much of py5's functionality is provided by the Processing core libraries. Py5 stands on the shoulders of giants.

- `Jonathan Feinberg <http://mrfeinberg.com/>`_ and the rest of the `Processing.py <https://py.processing.org/>`_ contributors. Processing.py is a Jython version of Processing, combining the same Processing core libraries that py5 utilizes with `Jython <https://www.jython.org/>`_, a Java implementation of Python. Processing.py is the spiritual ancestor to and inspiration for py5. Py5 is similar to Processing.py in that both use the Python programming language but their implementations are very different. Processing.py and py5 do not share any code but I know that there is code in the Processing core libraries written to accomodate Processing.py and that that code is also necessary for py5 to work correctly.

- I'd also like to thank Jonathan Feinberg for building the awesome Processing library `PeasyCam <http://mrfeinberg.com/peasycam/>`_. PeasyCam is one of the Processing libraries I know to work well in py5.

- The developers of the `JPype <https://github.com/jpype-project/jpype/>`_ and `PyJNIus <https://github.com/kivy/pyjnius>`_ Python libraries. Both of these libraries allow Python code to interact with Java code in the Java Virtual Machine using `JNI <https://en.wikipedia.org/wiki/Java_Native_Interface>`_. Py5 originally used PyJNIus but later switched to JPype. PyJNIus is maintained by the `Kivy <https://kivy.org/>`_ project (which I am a member of). JPype's lead developer `Thrameos <https://github.com/Thrameos>`_ introduced us to their library and motivated me to switch.

- `Lauren McCarthy <https://lauren-mccarthy.com/>`_, who created `p5.js <https://p5js.org/>`_, a JavaScript version of Processing. Lauren helped me understand the importance of developing the :doc:`Community`. It is from p5 that py5 gets its name.

- The ITP_ faculty, including `Tom Igoe <https://tigoe.com/>`_, `Dan Shiffman <https://shiffman.net/>`_, and `Allison Parrish <https://www.decontextualize.com/>`_. All provided early feedback that provided guidance and helped keep me motivated. Allison also helped me understand the importance and value of the integrating py5 with Jupyter notebooks. 

- The ITP_ residents of 2019 to 2020, for putting up with me and being available to bounce ideas off of as I was in the early stages of developing this idea.

.. _Processing: https://processing.org/
.. _ITP: https://tisch.nyu.edu/itp
