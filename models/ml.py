import pickle
import sklearn
import numpy as np
from sklearn.ensemble import RandomForestClassifier

_model_ = pickle.load(open("./models/random_forest.pkl", "rb"))


def get_prediction(
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
    para = np.array(
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
    y_pred = _model_.predict(para.reshape(1,11))
    print(y_pred)
    return y_pred


