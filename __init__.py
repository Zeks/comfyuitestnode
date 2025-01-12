import os

from .datastasher import CsvWriterNode
from .immature import ImmatureImageDataLoader
from .counter import ImmatureImageCounter

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "CsvWriterNode": CsvWriterNode,
    "ImmatureImageDataLoader": ImmatureImageDataLoader,
    "ImmatureImageCounter": ImmatureImageCounter,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "CsvWriterNode": "CSV Writer",
    "ImmatureImageDataLoader": "Immature Image Data Loader",
    "ImmatureImageCounter": "Immature Image Counter"
}

__all__ = NODE_CLASS_MAPPINGS


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
