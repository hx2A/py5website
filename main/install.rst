.. title: Install py5
.. slug: install
.. date: 2020-10-03 10:29:05 UTC-04:00
.. tags:
.. category:
.. link:
.. description: py5
.. type: text


.. contents:: Table of Contents
    :depth: 2

Anaconda
========

Anaconda is a widely used platform for working with Python and the open-source ecosystem. It makes it very easy to create and manage Python environments containing various Python libraries such as py5. Anaconda will also make it easy for you to use other popular Python tools such as Jupyter notebooks.

Install Anaconda
----------------

You will need to `download the Anaconda Installer for your Operating System <https://www.anaconda.com/products/individual>`_. Anaconda's `installation instructions <https://docs.anaconda.com/anaconda/install/>`_ are extensive and should be able to provide the necessary guidance for your computer.

Create Anaconda Environment
---------------------------

First you must create an Anconda environment to install the Python packages into. Below, we create an environment called ``py5coding`` with Python 3.8. Note that py5 does not support earlier versions of Python. Python 3.9 seems to work fine but has not been extensively tested.

The below command will also install the Jupyter notebooks tool, which py5 is designed to work well with.

.. code:: bash

    $ conda create -n py5coding python=3.8 notebook

After creating the ``py5coding`` environment you must "activate" it so that the subsequent commands take place inside of it. You will know you are inside the environment because your terminal prompt will change to include the name of the environment.

.. code:: bash

    (py5coding) $ conda activate py5coding

Install Java
------------

You will need to have Java 11 (or later) installed on your computer.

Before attempting the installation, first check to see if you already have it. You can do this from a terminal or DOS window using the command ``java -version``. 

.. code:: bash

    (py5coding) $ java -version
    openjdk version "11.0.9" 2020-10-20
    OpenJDK Runtime Environment 18.9 (build 11.0.9+11)
    OpenJDK 64-Bit Server VM 18.9 (build 11.0.9+11, mixed mode, sharing)

If you get an error or see the version number is 1.8 (which is likely for older computers), you will need to install Java. To install it into your Anaconda environment, use the below command.

.. code:: bash

    (py5coding) $ conda install -c conda-forge openjdk=11.0.8

If you prefer you can download and install Java 11 outside of the Anaconda environment. There are a lot of tutorials online that will explain how to do this for your computer. You don't have to use OpenJDK if you prefer a different environment. The only important requirement is that the command ``java -version`` gives the correct result.

.. IMPORTANT::
    It is important that you have Java 11 installed and available in the Anaconda environment because Processing 4 and therefore py5 both depend on it. If now or in the future you have the wrong version, you will see an error message stating that code "has been compiled by a more recent version of the Java Runtime".

    Be aware that someday Anaconda may want to downgrade your version of Java when you install some other package. Including the version number when installing (the ``=11.0.8`` in the previous command) will prevent this.

    For example, while testing these installation steps, I discovered than when I installed matplotlib with ``conda install matplotlib`` it would inexplicably want to downgrade Java 11 to Java 8. Why does it do this??? Matplotlib does not require Java, and doesn't attempt to install it at all if it was not previously installed into the Anaconda environment. Note that the workaround in that case is to install it with ``pip install matplotlib``, which doesn't have that problem. This was an easy fix but might trip up people who are new to Python.

Install Cairo and CairoSVG (optional)
-------------------------------------

Cairo is a drawing library for working with `Scalable Vector Graphics (SVG) <https://en.wikipedia.org/wiki/Scalable_Vector_Graphics>`_ files. If you complete this optional step, py5 will have the ability to convert SVG images to :doc:`py5image` objects using the :doc:`convert_image` method. As Cairo's ability to work with the SVG language is more complete than Processing's, this will provide better support for that image format.

Installing Cairo on Windows or Mac computers is difficult to impossible without using an Anaconda environment. To install it with Anaconda, use the below commands. The first installs Cairo and the second installs `CairoSVG <https://cairosvg.org/>`_, which is the Python library that py5 interfaces with to convert SVG images to Py5Image objects.

.. code:: bash

    (py5coding) $ conda install -c conda-forge cairo

You may get a message saying that it has already been installed. If so, rejoice and procede to the next step.

.. code:: bash

    (py5coding) $ pip install cairosvg

Install py5
-----------

Finally, install py5.

.. code:: bash

    (py5coding) $ pip install py5


Test Installation
-----------------

It is always a good idea to test that the installation was successful. Try the below commands to see if you can import py5. You will see an error if you have the wrong version of Java or if Java cannot be found.

.. code:: bash

    (py5coding) $ python
    Python 3.8.5 | packaged by conda-forge | (default, Sep 24 2020, 16:55:52)
    [GCC 7.5.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import py5
    >>> py5.__version__
    '0.3a3'

Updating py5
------------

Since py5 is a new library, you can expect frequent updates. Later you will want to upgrade your installation, which you can do with this command:

.. code:: bash

    (py5coding) $ pip install --upgrade py5
