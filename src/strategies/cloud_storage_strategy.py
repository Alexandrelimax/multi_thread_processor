from google.cloud import storage
from src.interfaces.storage_factory import StorageStrategy

class CloudStorageStrategy(StorageStrategy):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.client = storage.Client()

    def save(self, data, file_name):
        bucket = self.client.get_bucket(self.bucket_name)
        blob = bucket.blob(file_name)
        blob.upload_from_string(data)
        print(f"Data saved to Cloud Storage: {file_name}")