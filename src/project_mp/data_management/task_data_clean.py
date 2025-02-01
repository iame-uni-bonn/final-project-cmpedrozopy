# Pytask for processing the distance data
import pandas as pd

from project_mp.config import BLD, SRC
from project_mp.data_management.process_distance_data import (
    process_distance_data,
)


def task_process_distance_data(
    script=SRC / "data_management" / "process_distance_data.py",
    data=SRC / "data" / "Mission_coordinatesok.csv",
    produces=BLD / "data" / "distance_to_missions.pickle",
):
    """Clean the distance data set."""
    process_distance_data(data, produces)
    processed_data = pd.read_csv(produces, encoding="latin1")
    processed_data.to_pickle(produces)
