import os
from datetime import datetime

class ImmatureImageCounter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "date": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("file_count",)
    FUNCTION = "count_images"
    OUTPUT_NODE = True

    CATEGORY = "utils"

    def count_images(self, date):
        # Determine the correct date to use
        if not date:
            current_date = datetime.now().strftime("%Y-%m-%d")
        else:
            try:
                current_date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                return (0,)

        # Define the image folder path
        image_folder_path = f"ComfyUI/output/immaturate/{current_date}/immature"

        # Initialize PNG file count
        png_count = 0

        # Count PNG files in the specified folder
        if os.path.exists(image_folder_path) and os.path.isdir(image_folder_path):
            for filename in os.listdir(image_folder_path):
                print("filename is:", filename )
                if filename.lower().endswith('.png'):
                    png_count += 1

        return (png_count,)