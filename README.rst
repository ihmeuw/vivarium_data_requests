======================
Vivarium Data Requests
======================


This repository contains dummy data-loading components and model specifications
for fulfilling IHME client data requests using ``vivarium`` artifact building 
tools. All artifacts generated for clients should be replicable from the 
information contained here.

.. contents::

Creating an Environment
-----------------------

Whether you are generating a new artifact for a data request or reproducing
the artifact from an old request, you should make sure to work from a 
fresh ``conda`` environment.  You should install the ``vivarium_data_requests``
package in the clean environment and then install any additional requirements
from a ``requirements.txt`` file with **hard-pins** for all dependencies
associated with the data request.

New Data Requests
-----------------

**TODO**

Reproducing Artifacts from Previous Requests
--------------------------------------------

Individual data requests should be interacted with in a fresh ``conda``
environment. When reproducing a data request, install the top-level package and
then apply the relevant versioning information from the requirements file in the
subdirectory of interest.

``> pip install -r /path/to/requirements.txt``

Data requests are organized by approximate date and the requesting individual or
organization. Inside, there should be a ``requirements.txt`` file as well as a
README providing any extra information known. You will also find model_specifications
and any dummy components necessary to produce a data artifact to fulfill the
request. All that should be necessary is running

``> build_artifact -o /desired/output/path /path/to/model_spec.yaml``

unless otherwise specified in the README. 

NOTE: You must have access to IHME databases in order to build data artifacts.
