
import config
from results import cash_flow_projection


def main():
    maturity_period = 10
    loan_1 = cash_flow_projection.InterestIncome.create_interest_profile(maturity_period)
    print(loan_1.limit_profile)

if __name__ == '__main__':
    main()
