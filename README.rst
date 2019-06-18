vivarium_data_requests
======================

This repository contains dummy data-loading components and model specifications
for fulfilling data requests. It should be interacted with in a fresh conda
environment. When reproducing a data request, install the top-level package and
then apply the relevant versioning information from the requirements file in the
subdirectory of interest.

```pip install -r /path/to/requirements.txt```

Data requests are organized by approximate date and the requesting individual or
organization. Inside, there should be a requirements.txt file as well as a
README providing any extra information known. You will also find model_specifications
and any dummy components necessaryt to produce a data artifact to fulfill the
request. All that should be necessary is running

```build_artifact -o /desired/output/path /path/to/model_spec.yaml```

unless otherwise specified in the README.
