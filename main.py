from src.fetchers.data_fetcher import DataFetcher
from src.factory.storage_factory import StorageFactory

def main():
    base_url = "https://api.exemplo.com"
    
    endpoints = {
        'book': 'books/{item_id}',
        'price': 'books/{item_id}/price',
        'stock': 'books/{item_id}/stock'
    }
    
    book_ids = [1, 2, 3, 4, 5, ..., 1000]
    storage_type = "cloud_storage"

    config = {
        'bucket_name': 'my-bucket',
        'dataset_id': 'my_dataset',
        'table_id': 'books_table',
        'directory': '/local/storage/path'
    }

    data_fetcher = DataFetcher(base_url, endpoints, threads=5)

    print("Fetching data...")
    books_data = data_fetcher.fetch_all_data(book_ids)

    storage_strategy = StorageFactory.get_storage_strategy(storage_type, config)

    print("Saving data...")
    storage_strategy.save(books_data, "books_data.json")

    print("Data successfully fetched and saved.")

if __name__ == "__main__":
    main()
