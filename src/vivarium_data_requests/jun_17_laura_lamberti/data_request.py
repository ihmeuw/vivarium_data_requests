import warnings

import gbd_mapping
from vivarium_inputs.globals import DataDoesNotExistError


class ResearcherRequestComponent:
    """A one-off component to explicitly load data requested by an outside researcher/Abie"""

    def __init__(self):
        self.causes = [gbd_mapping.causes.neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma,
                       gbd_mapping.causes.neonatal_preterm_birth]

    def setup(self, builder):

        # Top-level things
        keys = [
            "population.structure",
            "population.theoretical_minimum_risk_life_expectancy",
            "cause.all_causes.cause_specific_mortality",
            "covariate.skilled_birth_attendance_proportion.estimate",
            "covariate.in_facility_delivery_proportion.estimate",
            "covariate.socio_demographic_index.estimate"
        ]
        for key in keys:
            try:
                builder.data.load(key)
            except DataDoesNotExistError:
                warnings.warn(f"no data found for key {key}.")
