import numpy as np


def calc_interest_income(interest_rate, drawn_profile):
    return np.multiply(interest_rate, drawn_profile)


def npv_interest_income(interest_income, discount_rate):
    return np.dot(interest_income, discount_rate)
