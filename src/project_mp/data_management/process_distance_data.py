import pandas as pd
import os   
import geopandas as gpd


def process_distance_data(input_file, output_file):
    """Load a CSV file, rename a column for easier merging.

    And save the processed data as a new CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the output CSV file.
    """
    distance_df = pd.DataFrame()
    distance_df = pd.read_csv(input_file, encoding="latin1")
    distance_df.rename(columns={"country": "mission_country"})
    distance_df.to_pickle(output_file)
    return distance_df

# Define the function to process shapefiles
def shape_to_csv(department_path, output_pickle):
    """Convert a shapefile to a pickle file, extracting centroid coordinates."""
    
    # Read and reproject the shapefile
    shape = gpd.read_file(department_path)
    shape = shape.to_crs(epsg=4326)

    # Calculate the centroid and extract the longitude and latitude
    shape["centroid"] = shape.centroid
    shape["longitude"] = shape["centroid"].x
    shape["latitude"] = shape["centroid"].y
    shape.drop(columns=["centroid"], inplace=True)  # Remove geometry column
    # Save as Pickle
    return shape

# Root directory containing the folders and shapefiles
#root_dir = "Users/moisespedrozo/Bonn/epp/shape_files"

# Go through all subdirectories and apply the function
#for root, dirs, files in os.walk(root_dir):
 #   for file in files:
  #      if file.endswith(".shp") and file.startswith("Distritos_"):
   #         department_path = os.path.join(root, file) 
    #        shape_to_csv(department_path)