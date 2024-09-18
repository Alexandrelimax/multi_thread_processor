from google.cloud import bigquery
from src.interfaces.storage_factory import StorageStrategy

class BigQueryStrategy(StorageStrategy):
    def __init__(self, dataset_id, table_id):
        self.client = bigquery.Client()
        self.dataset_id = dataset_id
        self.table_id = table_id

    def save(self, data, file_name=None):
        table_ref = f"{self.dataset_id}.{self.table_id}"
        errors = self.client.insert_rows_json(table_ref, data)
        if errors:
            raise RuntimeError(f"Failed to insert rows: {errors}")
        print("Data saved to BigQuery")