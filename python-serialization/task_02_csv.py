import csv
import json
"""Modules csv and json are imported to read CSV files and write JSON files respectively."""


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format and save it to 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to read from.

    Returns:
        bool: True if successful, False if an error occurs (like file not found).
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
