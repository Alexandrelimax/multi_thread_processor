import json
from src.interfaces.storage_factory import StorageStrategy

class LocalFileStrategy(StorageStrategy):
    def __init__(self, directory):
        self.directory = directory

    def save(self, data, file_name):
        file_path = f"{self.directory}/{file_name}"
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to local file: {file_path}")