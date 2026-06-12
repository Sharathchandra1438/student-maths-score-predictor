import os
import sys

from dataclasses import dataclass

import numpy as np

from sklearn.linear_model import(
    LinearRegression,
    Ridge,
    Lasso
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)

from sklearn.metrics import r2_score

from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:

    trained_model_file_path = os.path.join(
        "artifacts",
        "model.pkl"
    )

class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(
            self,
            train_array,
            test_array
    ):
        
        try:

            logging.info("Splitting training and test input data")

            X_train,y_train,X_test,y_test = (

                train_array[:, :-1],
                train_array[:, -1],

                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Linear Regression": LinearRegression(),

                "Lasso": Lasso(),

                "Ridge": Ridge(),

                "Decision Tree": DecisionTreeRegressor(),

                "Random Forest": RandomForestRegressor(),

                "Gradient Boosting": GradientBoostingRegressor(),

                "XGBoost": XGBRegressor(),

                "AdaBoost": AdaBoostRegressor()
            }

            params = {

                "Linear Regression": {},

                "Lasso": {
                    "alpha": [0.01, 0.1, 1, 10]
                },

                "Ridge": {
                    "alpha": [0.01, 0.1, 1, 10]
                },

                "Decision Tree": {
                    "criterion": ["squared_error", "friedman_mse"],
                    "splitter": ["best", "random"],
                    "max_depth": [None, 5, 10, 20]
                },

                "Random Forest": {
                    "n_estimators": [50, 100],
                    "max_depth": [None, 10, 20]
                },

                "Gradient Boosting": {
                    "learning_rate": [0.01, 0.1],
                    "n_estimators": [50, 100]
                },

                "XGBoost": {
                    "learning_rate": [0.01, 0.1],
                    "n_estimators": [50, 100]
                },

                "AdaBoost": {
                    "learning_rate": [0.01, 0.1],
                    "n_estimators": [50, 100]
                }
            }

            model_report = evaluate_models(
                X_train=X_train,
                y_train=y_train,

                X_test=X_test,
                y_test=y_test,

                models=models,
                params=params
            )

            best_model_score = max(
                sorted(model_report.values())
            )

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(
                    best_model_score
                )
            ]

            best_model = models[best_model_name]

            logging.info(
                f"Best Model Found: {best_model_name}"
            )


            if best_model_score < 0.6:
                raise CustomException(
                    "NO Best Model Found",
                    sys
                )
            
            save_object(

                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(
                y_test,
                predicted
            )


            return r2_square


        except Exception as e:

            raise CustomException(e, sys)

if __name__ == "__main__":

    from src.data_ingestion import DataIngestion

    from src.data_transformation import DataTransformation

    ingestion = DataIngestion()

    train_data, test_data = ingestion.initiate_data_ingestion()

    transformation = DataTransformation()

    train_arr, test_arr, _ = transformation.initiate_data_transformation(
        train_data,
        test_data
    )

    model_trainer = ModelTrainer()

    print(
        model_trainer.initiate_model_trainer(
            train_arr,
            test_arr
        )
    )