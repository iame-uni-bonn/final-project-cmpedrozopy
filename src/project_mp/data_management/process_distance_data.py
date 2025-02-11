import pandas as pd


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
