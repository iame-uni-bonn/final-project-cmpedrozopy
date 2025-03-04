# Pytask for processing the distance data
import pandas as pd
import os
import geopandas as gpd

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

def task_process_shapefiles(
    script = SRC / "data_management" / "process_distance_data.py",  
    root_dir = SRC / "data" / "Distritos_Alto_Parana.shp",
    output_dir = BLD / "data" / "alto_parana.pickle",
):
    """Convert shapefiles to CSV format, extracting centroid coordinates."""
    #shapefiles = [file for file in os.listdir(root_dir) if file.endswith(".shp") and file.startswith("Distritos_")]
    data = gpd.read_file(root_dir)
    data = shape_to_csv(data, output_dir)
    data.to_pickle(output_dir)