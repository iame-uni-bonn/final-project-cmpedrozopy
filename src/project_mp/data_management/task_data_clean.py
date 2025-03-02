# Pytask for processing the distance data
import pandas as pd

from project_mp.config import BLD, SRC
from project_mp.data_management.process_distance_data import (
    process_distance_data, shape_to_csv
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

def task_shape_to_csv(
    script=SRC / "data_management" / "process_distance_data.py",
    data=SRC / "data" ,
    produces=BLD / "data" / "distance_to_missions.pickle",
):
    """Clean the distance data set."""
    shape_to_csv(data, produces)
    processed_data = pd.read_csv(produces, encoding="latin1")
    processed_data.to_pickle(produces)
    return processed_data