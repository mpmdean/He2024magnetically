==========================================================
Data Repository
==========================================================
Source code and data files for the manuscript . Execute plot.ipynb to view the data.

How to cite
-----------
If this data is used, please cite W. He, Y. Shen, K. Wohlfeld, J. Sears, J. Li, J. Pelliciari, M. Walicki,
S. Johnston, E. Baldini, V. Bisogni, M. Mitrano, and M. P. M. Dean, Nature Communications (2024)


Run locally
-----------

Work with this by installing `docker <https://www.docker.com/>`_ and pip and then running

.. code-block:: bash

       pip install jupyter-repo2docker
       jupyter-repo2docker --editable .

Change `tree` to `lab` in the URL for JupyterLab.

Run remotely
------------

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/mpmdean/He2024magnetically/HEAD?filepath=plot.ipynb
