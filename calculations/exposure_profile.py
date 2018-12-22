import config
import numpy as np


def set_exposure_profile(amortisation_profile, initial_limit, initial_drawn, maturity):
    if amortisation_profile == config.bullet:
        limit_profile = np.ones(maturity) * initial_limit
        drawn_profile = np.ones(maturity) * initial_drawn
    else:
        # TODO: complete the amortisation profile calculations
        a = 1
    return [limit_profile, drawn_profile]
