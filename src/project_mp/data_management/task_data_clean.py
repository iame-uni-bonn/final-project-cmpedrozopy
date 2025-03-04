# Pytask for processing the distance data
import pandas as pd
import os

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

def task_process_shapefiles():
    """Convert shapefiles to CSV format, extracting centroid coordinates."""
    
    root_dir = SRC / "data" / "shape_files"
    output_dir = BLD / "data"
    #output_dir.mkdir(parents=True, exist_ok=True)  # Ensure BLD/data exists

    if not root_dir.exists():
        raise FileNotFoundError(f"Directory {root_dir} does not exist.")
    
    shapefiles = [file for file in os.listdir(root_dir) if file.endswith(".shp") and file.startswith("Distritos_")]
    
    for file in shapefiles:
        department_path = root_dir / file
        output_file = output_dir  / f"{file.replace('.shp', '.pkl')}" # #/ f"{file.replace('.shp', '.pkl')}"  # Ensure CSVs are saved in BLD/data
        shape_to_csv(department_path, output_file)
        #shape_file = pd.read_csv(output_file)
        #shape_file.to_pickle(output_file)