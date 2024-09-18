import requests
from concurrent.futures import ThreadPoolExecutor

class DataFetcher:
    def __init__(self, base_url, endpoints, threads=5):
        self.base_url = base_url
        self.endpoints = endpoints
        self.threads = threads

    def fetch_data(self, item_id):
        """
        Para cada item_id, faz uma requisição para cada endpoint no dicionário.
        return: Dicionário consolidado com os dados do item.
        """
        combined_data = {}
        for key, endpoint in self.endpoints.items():
            response = requests.get(f"{self.base_url}/{endpoint.format(item_id=item_id)}")
            if response.status_code == 200:
                combined_data[key] = response.json()
            else:
                combined_data[key] = None  # Tratar erro de resposta
        return combined_data

    def fetch_data_for_group(self, item_groups):
        """
        Processa um grupo de itens.
        return: Lista de dicionários com os dados de cada item no grupo.
        """
        return [self.fetch_data(item_id) for item_id in item_groups]

    def flatten_results(results):
        """
        Achata uma lista de listas em uma única lista.
        return: Lista achatada contendo todos os itens.
        """
        combined_results = []
        for group in results:
            for item in group:
                combined_results.append(item)
        return combined_results
    
    def fetch_all_data(self, item):
        """
        Divide os item em grupos e processa cada grupo em uma thread separada.
        return: Lista com os dados de todos os itens.
        """
        # Divide a lista de item em grupos
        group_size = len(item) // self.threads
        item_groups = [item[i:i + group_size] for i in range(0, len(item), group_size)]

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = list(executor.map(self.fetch_data_for_group, item_groups))
        
        # Como cada thread retorna uma lista de dados, precisamos combinar todas elas
        combined_results = self.flatten_results(results)
        return combined_results
