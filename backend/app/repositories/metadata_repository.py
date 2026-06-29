from app.schemas.dataset import DatasetCreate


class MetadataRepository:
    def __init__(self):
        self.datasets = []

    def create_dataset(self, dataset: DatasetCreate):
        self.datasets.append(dataset)
        return dataset

    def get_all_datasets(self):
        return self.datasets
    
metadata_repository = MetadataRepository()