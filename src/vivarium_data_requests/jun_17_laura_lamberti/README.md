A follow-up request from Laura Lamberti of BMGF on behalf of Hao Hu.
Unknown if it is for neonatal encephalopathy interventions or something
else.

The `run_all.py` script facilitates running making the data. Calling
it with 'create_specs' wil produce all the model specs, and subsequently
calling it with 'launch' will produce all the artifacts. Alternatively,
it can be called with 'run' followed by a model_spec name to produce
a single artifact. Normal `build_artifact` tools work, too, of course.

The covariate socio-demographic index appears to have no uncertainty for
these locations. This breaks the artifact building process due to
constraints enforced on the data. That specific constraint must be 
"turned off" manually in the sim validator file in vivarium_inputes
to proceed.

Indian states are determined programmatically by looking for location names
that contain India's location id in the path-to-global as well as either
'Urban' or 'Rural'.

