.. title: Reference Documentation Progress
.. slug: reference-documentation-progress
.. date: 2021-03-13 13:04:05 UTC-05:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Over the past month I've been pretty focused on improving the py5 Reference Documentation. Here's a quick update on what I've accomplished over the past month.

.. TEASER_END:

Reference Documentation Origins
===============================

First, note that all of the descriptions and example code you see in the `Processing reference documentation <https://processing.org/reference/>`_ was converted to py5 using an imperfect Python script I wrote specifically for this purpose. I put a lot of work into extracting useful documentation information from the Processing source and Processing documentation github repos. I'm extremely grateful to that the Processing library is well documented. It is because of this that py5's documentation has a solid foundation to build upon.

Descriptions
============

Previously, the py5 documentation descriptions were generally accurate but contained some content that was confusing, not applicable to Python, or just not true. There was also inconsistent formatting and other stylistic issues.

To fix this, I read through each description several times and made a lot of repairs. Now, all of the descriptions are accurate and well formatted.

Py5 makes new fields and methods available to users that previously were not documentated. Some of the new fields and methods are created by me, in Python, but others are public fields and methods in the Processing library that users could have always used had they known they existed. All of these new fields and methods currently have documentation that says "The documentation for this field or method has not yet been written." Originally there were over 200 fields and methods with such descriptions; now there are about 170. I'm doing a few each day. At first I thought this task would be insurmountable, but I am finding the work gives me an opportunity to think through the functionality more carefully and fix small mistakes I've made. The process is also oddly meditative and I'm happy to do it.

Example Code
============

Previously, most of the example code worked correctly, but a good portion of it was broken for various reasons. Also, all of the example code used "Imported Mode" (side note: "PDE Mode" will be renamed "Imported Mode").

Now all of the example code uses "Module Mode," and all of it works.

In the process of making these changes I also build the beginnings of a testing framework that will be useful later when I start writing unittests.

Next Steps
==========

Over the next month or two, I will be continuing to write the missing documentation descriptions. Just a few each day. I'll get there.

In other news, I now have a Mac computer. I bought a refurbished one and can use it to test and fix the py5 Mac issues. I'm making progress and will do a release when I can better support OSX.
