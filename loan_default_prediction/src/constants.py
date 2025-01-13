import os

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PATH_RAW_DATA = os.path.join(BASE_DIR, "data", "raw", "applicant_loan_data.csv")
PATH_VISUALIZATION_EDA = os.path.join(BASE_DIR, "visualizations", "EDA")
PATH_VISUALIZATION_EVAL = os.path.join(
    BASE_DIR, "visualizations", "modelling_evaluation"
)
