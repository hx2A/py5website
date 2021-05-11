.. title: Finished Reference Documentation
.. slug: finished-reference-documentation
.. date: 2021-05-10 20:48:05 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

I've done it. I finished the `py5 Reference Documentation <link://filename/reference/index.rst>`_.

This was an indescribable amount of work. I first mentioned it in December in my second blog post, :doc:`start-of-reference-documentation`. The actual work started at least two months before that. Between then and now I also had surgery once and weathered several a few personal and family problems. On top of pandemic issues. I persevered.

.. TEASER_END:

Completing the documentation was by far the most critical and onerous part of this project. It wasn't just about writing blocks of text for each field and method. Much of the reference documentation and examples are Python or py5 versions of Processing's documentation. As always, I wrote Python code to help with the necessary text and code transformations. Of course no Python program can transform this perfectly; everything had to be read and reviewed by me for accuracy and truthfulness. While doing this, I found and fixed a lot of little bugs. Since py5 leverages the Processing Java libraries to provide the functionality, and since this is essentially a metaprogramming project, getting 90% of the library to work was easy, but getting the remaining 10% to work was tedious and time consuming. And without that 10%, I don't have a library that would be useable to anyone. This had to be done.

Now I feel I am well positioned for the future. There might still be some small errors or shortcomings in the reference documentation, but for the most part, it is a source of truth about py5 and how everything actually works. That's what I'm most excited about right now. All of the example code actually runs, and I have a script that can re-run everything. Eventually I will create unit tests around the example code and integrate that into the build process via GitHub Actions. It's going to be great.

So what's next? I've been focused on reference documentation for so long, I hardly know what to do with myself now.

I know what's next: I have `several important bugs <https://github.com/hx2A/py5generator/issues>`_ I need to fix. I'm going to start with the Jupyter Lab bug and then try to make some progress on the OSX bugs. I'd like to do a release in the next week or two.
