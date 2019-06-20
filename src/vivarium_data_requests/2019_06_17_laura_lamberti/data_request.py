import warnings

import gbd_mapping
from vivarium_inputs.globals import DataDoesNotExistError


class ResearcherRequestComponent:
    """A one-off component to explicitly load data requested by an outside researcher/Abie"""

    def __init__(self):
        self.causes = [gbd_mapping.causes.neonatal_encephalopathy_due_to_birth_asphyxia_and_trauma,
                       gbd_mapping.causes.neonatal_preterm_birth]
    @property
    def name(self):
        return "researcher_request_component"

    def setup(self, builder):

        # Top-level things
        keys = [
                # pop info
            "population.structure",
            "population.theoretical_minimum_risk_life_expectancy",
                # what was asked for
            "covariate.skilled_birth_attendance_proportion.estimate",
            "covariate.in_facility_delivery_proportion.estimate",
            "covariate.socio_demographic_index.estimate",
                # for fun
            "covariate.healthcare_access_and_quality_index.estimate",
            "covariate.hospital_beds_per_1000.estimate",
                # components of SDI
            "covariate.total_fertility_rate.estimate",
            "covariate.gdp_per_capita_base_2010.estimate",
            "covariate.maternal_education_years_per_capita.estimate"
        ]
        for key in keys:
            try:
                builder.data.load(key)
            except DataDoesNotExistError:
                warnings.warn(f"no data found for key {key}.")
