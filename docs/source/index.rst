.. DiagramDigitizer documentation master file, created by
   sphinx-quickstart on Thu May 13 21:08:26 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Software for data extraction from plots and images
==================================================

DiagramDigitizer is an easy-to-use tool to extract numerical data from plots and images and export them for further
use.

DiagramDigitizer has the following capabilities:

- Import of diagrams in different image file formats.
- Extraction of data from diagrams by mouse.
- Data organization in different data sets.
- Handling of different axes scales: linear and logarithmic.
- Zooming of diagrams.
- Various export formats: Text, CSV, and Excel. Special feature: The Excel sheet additionally contains a chart with the digitized data points.
- Processing of numerical data before export: Sorting and interpolation.

Everybody is welcome to use DiagramDigitizer. 

Audience
--------

The audience for DiagramDigitizer includes engineers, mathematicians, physicists, biologists, and anyone else
who intends to convert plots into numerical data.

License
-------

Copyright (C) 2016-2021 Michael Fischer.

DiagramDigitizer is open source software; you can redistribute it and/or modify it under the terms of
the :doc:`GPL-3.0 </license>`.

History
-------

DiagramDigitizer was born in January 2016. The software was designed and written by Michael Fischer.

Installation
------------

DiagramDigitizer requires Python 3.6, 3.7, or 3.8 and builds upon PyQt5. It can be installed from Anaconda prompt
using ``pip``.

.. code:: bash

    pip install diagramdigitizer

Quick start
-----------

After installation DiagramDigitizer can be started from Anaconda prompt by

.. code:: bash

    diagramdigitizer

or from Python prompt by

.. code:: python

    >>> import diagramdigitizer
    >>> diagramdigitizer.diagramdigitizer.run()

Tutorial
--------

An examplary application of the software is presented in the :doc:`tutorial <tutorial>`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
