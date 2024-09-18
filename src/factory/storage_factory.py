from src.strategies.cloud_storage_strategy import CloudStorageStrategy
from src.strategies.bigquery_strategy import BigQueryStrategy
from src.strategies.local_file_strategy import LocalFileStrategy

class StorageFactory:
    @staticmethod
    def get_storage_strategy(storage_type, config):
        strategies = {
            'cloud_storage': CloudStorageStrategy(config['bucket_name']),
            'bigquery': BigQueryStrategy(config['dataset_id'], config['table_id']),
            'local_file': LocalFileStrategy(config['directory'])
        }

        if storage_type not in strategies:
            raise ValueError(f"Unknown storage type: {storage_type}")
        
        return strategies[storage_type]