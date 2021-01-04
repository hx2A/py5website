.. title: Start of Reference Documentation
.. slug: start-of-reference-documentation
.. date: 2020-12-01 08:54:59 UTC-05:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

After a great struggle, I finally coded the basic structure of the `py5 Reference Documentation <link://filename/reference/index.rst>`_. This was a rather intimidating task and probably one of the last difficult technical challenges I faced for the initial phase of this project.

.. TEASER_END:

Look at the documentation for the :doc:`rect` method. You'll see the layout is analogous to the `Processing rect documentation <https://processing.org/reference/rect_.html>`_. There are even links to the underlying Processing documentation when py5 makes calls to Processing.

The description texts and example code snippets all come from the Processing documentation with some automated modifications to translate Java code to Python. Because the translations were done with code, there are some errors. Still, the automated process did much of the work for me and will save me a lot of time as I finalize the documentation.

Currently, the reference documentation is incomplete. The py5 library exposes the public Processing methods and fields that had no documentation available for them. This is frequently the case for the methods and fields in the ancillary classes like :doc:`py5shape`. There is also no documentation for new features added by me like :doc:`np_pixels` or :doc:`lines`. I have a lot of work ahead of me to write all of the missing documentation.

I'm quite pleased that the contents of the py5 Python docstrings and the documentation you see on this website come from `the same source files <https://github.com/hx2A/py5generator/tree/master/py5_docs/Reference/api_en/>`_. I put a lot of work into that. This setup also supports my multilingual ambitions for py5. Once I complete the English documentation, I can translate it to other languages. Not only will I have multilingual reference documentation for this website, I'll be able to produce multiple versions of py5, each with the docstrings in a different language. And I'll do it in a way that will be easy to maintain. I know of no other Python library that can do this.
