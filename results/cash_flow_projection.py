import numpy as np


class InterestIncome(object):

    def __init__(self, maturity_period):
        # initialise individual arrays required to calculate the cash flow
        self.limit_profile = np.zeros(maturity_period)
        self.drawn_profile = np.zeros(maturity_period)
        self.discount_rate = np.zeros(maturity_period)
        self.ibor_interest_income = np.zeros(maturity_period)
        self.rfr_interest_income = np.zeros(maturity_period)

    def set_exposure_profile(self, limit_profile, drawn_profile):
        self.limit_profile = limit_profile
        self.drawn_profile = drawn_profile

    @staticmethod
    def create_interest_profile(maturity_period):
        interest_income = InterestIncome(maturity_period)
        return interest_income
