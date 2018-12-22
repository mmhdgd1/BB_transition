import numpy as np


class EconomicImpact(object):

    def __init__(self, maturity_period):
        # initialise individual arrays required to calculate the cash flow
        self.limit_profile = np.zeros(maturity_period)
        self.drawn_profile = np.zeros(maturity_period)
        self.discount_rate = np.zeros(maturity_period)
        self.ibor_interest_income = np.zeros(maturity_period)
        self.rfr_interest_income = np.zeros(maturity_period)

