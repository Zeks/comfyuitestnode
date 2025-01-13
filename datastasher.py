import os
import csv
from datetime import datetime

class CsvWriterNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 23948457612}),
                "width": ("INT", {"default": ""}),
                "height": ("INT", {"default": ""}),
                "body": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "writeToCSV"
    OUTPUT_NODE = True  # This node will perform a write operation and does not return anything to the pipeline.

    CATEGORY = "utils"

    def writeToCSV(self, seed, width, height, body):
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Define the CSV file name and path
        csv_filename = f"ComfyUI/output/rapidfire/{current_date}/data.csv"

        # Ensure the 'data' directory exists
        os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

        # Get the current time in the format HH:MM:SS
        current_time = datetime.now().strftime("%H:%M:%S")

        # Prepare the row to be written
        row_to_write = [current_time, str(seed), width, height, body]

        # Determine if we need to write headers (if file does not exist)
        needs_header = not os.path.exists(csv_filename) or os.stat(csv_filename).st_size == 0

        with open(csv_filename, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            if needs_header:
                # Write headers
                writer.writerow(["timestamp", "seed",  "width", "height", "body"])

            # Write the row to the CSV file
            writer.writerow(row_to_write)

        return ()

