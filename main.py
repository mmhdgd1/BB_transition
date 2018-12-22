
import config
import numpy as np
from results import cash_flow_projection
from calculations import interest_income_profile, exposure_profile


def main():
    # setting variables
    maturity_period = 10
    initial_limit = 1000
    initial_drawn = 500
    amortisation_profile = "bullet"
    interest_rate = np.ones(maturity_period)
    test_loan = cash_flow_projection.EconomicImpact(maturity_period)
    [test_loan.limit_profile, test_loan.drawn_profile] = (
        exposure_profile.set_exposure_profile(amortisation_profile, initial_limit, initial_drawn, maturity_period)
    )
    test_loan.ibor_interest_income = \
        interest_income_profile.calc_interest_income(interest_rate, test_loan.drawn_profile)
    test_loan.rfr_interest_income = \
        interest_income_profile.calc_interest_income(interest_rate, test_loan.drawn_profile)


if __name__ == '__main__':
    main()
