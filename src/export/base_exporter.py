import abc

import pandas as pd


class BaseExporter:
    def __init__(self):
        pass

    @abc.abstractmethod
    def export(self, df: pd.DataFrame):
        raise NotImplementedError


class CSVExporter(BaseExporter):
    def __init__(self):
        super().__init__()

    def export(self, df: pd.DataFrame):
        pass
