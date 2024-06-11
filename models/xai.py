import shap
from .ml import _model_
from .user_data import UserData

_explainer_ = shap.Explainer(_model_)


def get_explanation(user_data: UserData):
    shap_values = _explainer_.shap_values(user_data.data_arr.reshape(1, 11))
    print(shap_values)
    return shap_values
