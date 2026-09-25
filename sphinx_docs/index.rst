tensor_utils
============

Personal Python utility functions for manipulating data tensors.

Installation
------------

.. code-block:: bash

   pip install git+https://github.com/pushkar5586/tensor_utils.git

Quick example
-------------

.. code-block:: python

   import numpy as np
   from tensor_utils import add_past_windows

   A = np.arange(10)
   windows = add_past_windows(A, lb=3, strict_lookback=True)

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api
