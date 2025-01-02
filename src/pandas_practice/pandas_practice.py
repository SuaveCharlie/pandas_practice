import logging

from src.data_loader.base_data_loader import BaseDataLoader
from src.export.base_exporter import BaseExporter
from src.transformers.base_transformer import BaseTransformer


class PandasPractice:
    """Orchestrator class that takes the different components and runs the commands"""

    def __init__(
        self,
        data_loader: BaseDataLoader,
        transformer: BaseTransformer,
        exporter: BaseExporter,
    ):
        logging.info(data_loader)
        logging.info(type(data_loader))
        self.data_loader = data_loader
        self.transformer = transformer
        self.exporter = exporter

    def run(self):
        data = self.data_loader.load_data()
        validated_transformed_data = self.transformer.transform(data)
        self.exporter.export(validated_transformed_data)
