"""
This script tranform a folder of csvs to a single xlsx file with each csv as a sheet.
"""

import pandas as pd
import os


def csvs_to_xlsx(csv_folder : str, xlsx_file : str):
    """
    This function takes a folder of csv files and transforms them into a single xlsx file with each csv as a sheet.

    :param csv_folder: str
    :param xlsx_file: str
    """
    # Get all csv files in the folder
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]
    # Create the xlsx file
    xlsx_file = os.path.join(csv_folder, xlsx_file)

    # Create a writer object
    writer = pd.ExcelWriter(xlsx_file, engine='xlsxwriter')

    # Iterate over each csv file
    for csv_file in csv_files:
        # Read the csv file
        df = pd.read_csv(os.path.join(csv_folder, csv_file))

        # Write the csv file to the xlsx file
        df.to_excel(writer, sheet_name=os.path.splitext(csv_file)[0], index=False)

    # Save the xlsx file
    writer._save()

if __name__ == '__main__':
    csvs_to_xlsx('output', 'output.xlsx')

