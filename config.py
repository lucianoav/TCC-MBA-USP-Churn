# configurações globais do projeto

import os
from pathlib import Path
import pandas as pd

# paths absolutos
PROJECT_ROOT = Path(__file__).parent

# paths relativos
DATA_PATH = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_PATH / "raw"
PROCESSED_DATA_PATH = DATA_PATH / "processed"
MODELS_PATH = PROJECT_ROOT / "models"
SUBMISSIONS_PATH = PROJECT_ROOT / "submissions"
REPORTS_PATH = PROJECT_ROOT / "reports"
NOTEBOOKS_PATH = PROJECT_ROOT / "notebooks"

# cofigurações
RANDOM_STATE = 1234
TEST_SIZE = 0.2
CV_FOLDS = 5

# força download dos dados brutos - substitui dados caso já existam na pasta RAW_DATA_PATH
FORCE_DOWNLOAD = False

# competição
KAGGLE_COMPETITION = " "

# features e target
TARGET = "Exited"

NUMERICAL_FEATURES = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
CATEGORICAL_FEATURES = ['Geography', 'Gender', 'HasCrCard', 'IsActiveMember']
IGNORE_FEATURES = ['RowNumber', 'CustomerId', 'Surname']

# tipo de problema "classification" ou "regression"
PROBLEM_TYPE = "classification"
