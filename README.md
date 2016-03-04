# CMI Exchange

This project is a community developed collection of sample scripts, functions
and IPython plugins related to the DiffPy-CMI complex modeling framework.
If you are new to DiffPy-CMI, browse through the [available files](./cmi_scripts/) to get a feel for
what DiffPy-CMI can do.  If you've written a useful or instructive piece of code using any
part of the DiffPy-CMI framework, feel free to share your work with the community.
If you are new to git and would like to learn how to contribute
[start here](https://help.github.com/articles/fork-a-repo).

New User Tips
-------------

To get started, using the button on the right download the zip file (or clone this project to your local machine). Once you have the files
the best way to run the examples is to use [IPython](http://ipython.org) with interactive plotting. [IPython](http://ipython.org) is a powerful command line Python environment that we heavily utilize in the project. If you've followed the installation instructions for DiffPy-CMI it should already be installed.

For example,
to simulate the PDF of C60, navigate to the [cmi_scripts/calcpdfc60](./cmi_scripts/calcpdfc60) directory and
type:

    $ ipython --pylab
    In [1]: %run c60.py


Some of the examples are written as a Jupyter Notebooks (extension
.ipynb).  The Jupyter Notebook creates an interactive computational environment
similar to Mathematica.  To start a notebook session, run the command

    $ jupyter notebook

You can then load the .ipynb file directly into your workspace.


### Recommended Tutorials

* [Fit Ni PDF](./cmi_scripts/fitNiPDF)

Contents
---------

* [cmi_plugins](./cmi_plugins/) contains IPython plugins and functions.
* [cmi_scripts](./cmi_scripts/) contains complete python scripts that make use of the DiffPy-CMI packages.
