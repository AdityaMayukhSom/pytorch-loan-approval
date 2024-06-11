import numpy as np


class UserData:
    def __init__(
        self,
        no_of_dependents: int,
        education: str,
        self_employed: str,
        income_annum: int,
        loan_amount: int,
        loan_term: int,
        cibil_score: int,
        residential_assets_value: int,
        commercial_assets_value: int,
        luxury_assets_value: int,
        bank_asset_value: int,
    ):
        self.no_of_dependents = no_of_dependents
        self.education = education
        self.self_employed = self_employed
        self.income_annum = income_annum
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.cibil_score = cibil_score
        self.residential_assets_value = residential_assets_value
        self.commercial_assets_value = commercial_assets_value
        self.luxury_assets_value = luxury_assets_value
        self.bank_asset_value = bank_asset_value
        self.data_arr = np.array(
            [
                no_of_dependents,
                education,
                self_employed,
                income_annum,
                loan_amount,
                loan_term,
                cibil_score,
                residential_assets_value,
                commercial_assets_value,
                luxury_assets_value,
                bank_asset_value,
            ]
        )
