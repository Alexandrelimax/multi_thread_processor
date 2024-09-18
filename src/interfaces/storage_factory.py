from abc import ABC, abstractmethod

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, data, file_name):
        """Método que todas as estratégias de armazenamento devem implementar"""
        pass