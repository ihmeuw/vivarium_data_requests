
This is a request for data from Laura Lamberti of BMGF on behalf of Hao Hu.
The data is requested for work on Neonatal Encepholopathy interventions.

The `run_all.py` script facilitates making the data. Calling
it with 'create_specs' wil produce all the model specs, and subsequently
calling it with 'launch' will produce all the artifacts. Alternatively,
it can be called with 'run' followed by a model_spec name to produce
a single artifact. Normal `build_artifact` tools work, too, of course.

This archive is being prepared after the fact. It appears that at least
some of the data pertaining to India subnational locations have changed 
in between the fulfillment of the request and now. In addition, an 
extra location, Sri Lanka, was added after the original request. It is
documented here as well.

Note:
Some of these supernational locations contain populations large enough
to break raw validation limits. These particular data artifacts must be
made under an altered vivarium_inputs installation. The raw population
structure validation's upper limit MAX_POP and the sim population
structure validation's upper limit in VALID_POPULATION_RANGE should be
increased to allow these populous regions.

