import pickle
import numpy as np
from .user_data import UserData

_model_ = pickle.load(open("./models/random_forest.pkl", "rb"))


def get_prediction(user_data: UserData):
    y_pred = _model_.predict(user_data.data_arr.reshape(1, 11))
    print(y_pred)
    return y_pred
