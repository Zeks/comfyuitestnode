import os
from datetime import datetime
import csv

class ImmatureImageDataLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", {"default": 0}),
                "date": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ( "INT","STRING","STRING","STRING")
    RETURN_NAMES = ("seed","image_name", "headings_illustrous", "prompt")
    OUTPUT_NODE = True
    
    FUNCTION = "loadImageData"

    CATEGORY = "utils"

    def loadImageData(self, index, date):
        print("LOADING DATA")
        # Determine the correct date to use
        if not date:
            current_date = datetime.now().strftime("%Y-%m-%d")
            print("current date will be", current_date)
        else:
            try:
                current_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                print("VALUE ERROR")
                return (0, "", "", "", "")

        # Define the image folder path
        image_folder_path = f"ComfyUI/output/immaturate/{current_date}/immature"

        # Ensure the 'data' directory exists and get the CSV file name
        path, filename = os.path.split(os.path.realpath(__file__))
        csv_filename = f"{path}/data/{current_date}.csv"

        # Initialize dictionaries for filenames and CSV data
        image_filenames_dict = {}
        csv_data_by_seed = {}
        # Read image filenames from the folder
        if os.path.exists(image_folder_path) and os.path.isdir(image_folder_path):
            print("READING IMAGE FOLDER")
            for filename in os.listdir(image_folder_path):
                if filename.lower().endswith('.png'):
                    root, _ = os.path.splitext(filename)
                    fullpath = os.path.join(image_folder_path, filename)
                    image_filenames_dict[root] = fullpath
        else:
            print("image folder does not exist", image_folder_path)

        # Read CSV data and index by 'seed'
        if os.path.exists(csv_filename) and os.path.isfile(csv_filename):
            print("READING CSV FILE")
            with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    seed = int(row["seed"])
                    csv_data_by_seed[seed] = {
                        "imagename": "",
                        "prompt_headings_a": row.get("prompt_headings_a", ""),
                        "prompt_body": row.get("prompt_body", "")
                    }
        else:
            print("csv file does not exist",csv_filename)                    

        # Match image filenames with CSV data
        for filename, fullpath in image_filenames_dict.items():
            seed = int(filename)
            if seed in csv_data_by_seed:
                csv_data_by_seed[seed]["imagename"] = fullpath

        # Get the list of seeds from image_filenames_dict
        sorted_seeds = [int(filename) for filename in image_filenames_dict.keys()]

        # Find the data corresponding to the provided index
        if 0 <= index < len(sorted_seeds):
            seed = sorted_seeds[index]
            csv_entry = csv_data_by_seed.get(seed, {})

            return (
                seed,
                csv_entry.get("imagename", ""),
                csv_entry.get("prompt_headings_a", ""),
                csv_entry.get("prompt_body", "")
            )
        else:
            # If index is out of range, return default values
            return (0, "", "", "")
